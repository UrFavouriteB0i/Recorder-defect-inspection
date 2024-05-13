import sys, threading
import serial.tools.list_ports
import cv2
import numpy as np
import mvsdk
from threading import Thread, Event
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QCoreApplication, QThread, Signal, Slot, QObject
from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtMultimedia import QMediaDevices
from SDKtool import Camera
from ui_Main import Ui_MainWindow        
       

class CameraProccess(QThread):
    Image=Signal(QImage)
    ImageProcess = Signal(QImage)
    ImageCaptured = Signal(QImage)
    

    def run(self):
        global camIndex, camState
        global InspectState
        global GrayCB, NoRedCB, HistCB, roiCB, TmpMatCB, BlobCB
        
        global cap_img
        global status

        if camState == "SYS":
            self.capture = cv2.VideoCapture(0)
            self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
            self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,640)
        
        elif camState == "MV":
            self.capture = Camera(DeviceList.DevList[camIndex])
            if self.capture.open():
                print(self.capture)
        
        self.ThreadActive = True
        
        while self.ThreadActive:
            if camState == "SYS":
                ret, frame = self.capture.read()
                flip_frame = cv2.flip(src=frame, flipCode=1)

            elif camState == "MV":
                frame = self.capture.grab()
                frame = cv2.resize(frame, (640, 480), interpolation= cv2.INTER_LINEAR)

            if frame is not None:
                
                frame_rgb = cv2.cvtColor(flip_frame, cv2.COLOR_BGR2RGB)
                height, width, channel = frame_rgb.shape
                q_img = QImage(frame_rgb.data, width, height, width * channel, QImage.Format_RGB888)
                
                #self processing frame
                if InspectState == 0:
                    p_img = q_img
                    s_img = QImage()
                    
                elif InspectState == 1:
                    p_img = self.ProcessImage(frame)

                    if status == "show":
                        s_img = self.captureImage(p_img)
                        status = "wait"
                
                    elif status == "wait":
                        pass
                
                else: 
                    s_img = QImage()           


                #Self capturing frame
                self.Image.emit(q_img)
                self.ImageProcess.emit(p_img)
                self.ImageCaptured.emit(s_img)


    def stop(self):
        self.ThreadActive = False
        self.quit()
        
            
    def ProcessImage(self, frame):
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply noise reduction (Gaussian blur)
        blurred_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)

        # Apply histogram equalization
        equalized_frame = cv2.equalizeHist(blurred_frame)

        # Perform ROI extraction
        # Example: Define region of interest (ROI) coordinates
        roi_x, roi_y, roi_width, roi_height = 100, 100, 200, 200
        roi = equalized_frame[roi_y:roi_y + roi_height, roi_x:roi_x + roi_width]

        # Perform blob analysis
        _, thresholded_roi = cv2.threshold(roi, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        contours, _ = cv2.findContours(thresholded_roi, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Draw ROI rectangle on the original frame
        frame_with_contours = frame.copy()
        cv2.rectangle(frame_with_contours, (roi_x, roi_y), (roi_x + roi_width, roi_y + roi_height), (0, 255, 0), 2)

        # Draw contours within the ROI
        for contour in contours:
            contour += (roi_x, roi_y)  # Shift contour coordinates to match ROI position
            cv2.drawContours(frame_with_contours, [contour], -1, (0, 0, 255), 2)

        # Convert processed frame back to QImage
        height, width, channel = frame_with_contours.shape
        bytes_per_line = 3 * width
        q_img_prc = QImage(frame_with_contours.data, width, height, bytes_per_line, QImage.Format_BGR888)
        
        return q_img_prc
    
    def captureImage(self, img):
            global status
            i = 0
            if i==0:
                result = img
                status = ""
                i = 1
            else: pass

            return result


class ComPort():
    ports = serial.tools.list_ports.comports()
    serialInst = serial.Serial()
    portslist = []
    for one in ports:
        portslist.append(str(one))


class DeviceList(QCoreApplication):
    global cam

    #Check Camera from System
    Cameras = QMediaDevices.videoInputs()
    CamList = []
    for cam in Cameras:
        print(cam.description())
        CamList.append(str(cam.description()))

    #Check Camera from MVSDK Device
    DevList = mvsdk.CameraEnumerateDevice()
    nDev = len(DevList)
    hlist = []
    idx = 0
    
    if nDev < 1:
        print("No MV Cam Found! Skipping..")

    else:
        for DevInfo in DevList:
            print(DevInfo.GetFriendlyName())
            hlist.append(DevInfo.GetFriendlyName())
            cam = Camera(DevList[0])


class mainWindow(QMainWindow, Ui_MainWindow):
    s = 0
        
    def __init__(self):
        global camIndex

        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Recorder Inspection Monitor V1.0")
        self.resize(1280,800)
        
        #Set-up Menubar function
        self.actionAbout_Software.triggered.connect(self.about_sftwr)

        #Setup Initial UI Condition
        
        #Setup combobox Value
        self.ComboPort.addItems(ComPort.portslist)
        self.ComboCam.addItems(DeviceList.hlist)
        self.ComboCam.addItems(DeviceList.CamList)   

        #Setup Signal & Slot Connection
        self.ComboPort.activated.connect(self.showOKbutton)
        self.ComboCam.activated.connect(self.showOKbutton)
        self.OkButton.clicked.connect(self.submitCOMcam)
        self.AutoButton.clicked.connect(self.Auto_Mode)
        self.ManualButton.clicked.connect(self.Manual_Mode)
        self.StartButton.clicked.connect(self.StartCam)
        self.StopButton.clicked.connect(self.StopCam)
        self.InspectButton.clicked.connect(self.Inspect)
        self.StoppButton.clicked.connect(self.Auto_Mode_stop)

        self.actionQuit.triggered.connect(self.quit_app)
        
        #Setup Initial widget state
        self.OkButton.setDisabled(True)
        self.AutoButton.setDisabled(True)
        self.ManualButton.setDisabled(True)
        self.StartButton.setDisabled(True)
        self.StopButton.setDisabled(True)
        self.GripButton.setDisabled(True)
        self.RotateButton.setDisabled(True)
        self.InspectButton.setDisabled(True)
        self.StoppButton.setDisabled(True)

        self.groupBox_5.setDisabled(True)

    #========== GUI's visual Function Definition ============#
    def showOKbutton(self):
        if self.s==1:
            self.OkButton.setEnabled(True)
        else:
            self.s+=1

    def Auto_Mode(self):
        global status, InspectState
        
        InspectState = 0
        status = ""

        self.CameraON()
        self.groupBox_3.setDisabled(True)
        self.groupBox_5.setDisabled(True)
        self.ManualButton.setDisabled(False)
        self.AutoButton.setDisabled(True)
        self.InspectButton.setDisabled(False)

    def Manual_Mode(self):
        self.ManualButton.setDisabled(True)
        self.StartButton.setDisabled(False)
        self.StopButton.setDisabled(False)

    def Inspect(self):
        global InspectState

        try:
            InspectState = 1

            self.InspectButton.setDisabled(True)
            self.StoppButton.setDisabled(False)
            
            #Arduino command
            self.Worker2_Arduino = Thread(target=self.ArduinoCOM)
            self.Worker2_Arduino.start()

        except:
            return "Error"
        
    #========== GUI's action Function Definition ============#  

    def CameraON (self):
        self.Worker1_Opencv = CameraProccess()
        self.Worker1_Opencv.Image.connect(self.cam_emit)
        self.Worker1_Opencv.ImageProcess.connect(self.openCV_emit)
        self.Worker1_Opencv.ImageCaptured.connect(self.Capture_emit)
        self.Worker1_Opencv.start()

    def submitCOMcam(self):
        mainWindow.s = 0
        global camIndex, camState, Port

        #COM Port connection
        Port = ComPort.serialInst
        Portnum = self.ComboPort.currentText()
        Port.port = "COM24" #self.Portnum
        Port.baudrate = 9600
        
        try:
            Port.open()
            Port.write("Opening COM Test Message".encode('utf-8'))

        except SyntaxError as e:
            return e.msg

        #Device & Camera connection
        camText = self.ComboCam.currentText()
        
        if camText in DeviceList.CamList:
            camState = "SYS"
            camIndex = self.ComboCam.currentIndex()
            if camIndex == 0: camIndex +=1
            elif camIndex == 1: camIndex -=1
            
            print("Connected to Camera from System")

        elif camText in DeviceList.hlist:
            camState = "MV"
            camIndex = DeviceList.hlist.index(camText)
            print("Connected to MV Camera")

        self.OkButton.setDisabled(True)
        self.AutoButton.setDisabled(False)
        self.ManualButton.setDisabled(False)
    
    def ArduinoCOM(self):
        global status

        self.command = "GRIP"
        i = 0 
        #make sure thread always run unless need to stop
        
        while True:
            #Check if there's any value waiting in input buffer

            while Port.in_waiting==0:
                #Do something
                #1. Grip Component or Rotate Component
                if self.command == "":
                    pass
                elif self.command == "GRIP":
                    Port.write(self.command.encode('utf-8'))
                    self.command = ""
                elif self.command == "RTT":
                    Port.write(self.command.encode('utf-8'))
                    self.command = ""
                elif self.command == "UNGRIP":
                    Port.write(self.command.encode('utf-8'))
                    self.command = ""
                else: pass

            r_packet = Port.readline().decode('utf-8')
            r_packet = r_packet.strip('\r\n')

            #Check Condition and assign value
            if r_packet == "FINISH GRIP":
                print(r_packet)
                status = "show"
                self.command = "RTT"

            elif r_packet == "FINISH ROTATE" and i < 6:
                if self.statsLabel.text != "STATUS: DEFECT":
                    print(r_packet)
                    status = "show"
                    self.command = "RTT"
                    i+=1
                elif self.statsLabel.text == "STATUS: DEFECT":
                    print("Arduino Thread finish working")
                    Port.close()
                    
            elif r_packet =="FINISH ROTATE" and i == 6:
                print("Arduino Thread finish working")
                Port.close()
                   
        
    def Auto_Mode_stop(self):
        self.StoppButton.setDisabled(True)
        self.InspectButton.setDisabled(False)
        self.statsLabel.setText("STATUS: Stopping")
        
        try:
            self.Worker1_Opencv.stop()
            self.openCV_stop_emit()
        
        except TypeError as e:
            return e
        
        self.statsLabel.setText("STATUS:")
        
    def StartCam(self):
        self.StartButton.setDisabled(True)
        self.StopButton.setDisabled(False) 

    def StopCam(self):
        self.StopButton.setDisabled(True)
        self.StartButton.setDisabled(False)
        self.Worker1_Opencv.stop()
        self.openCV_stop_emit()
    
    def cam_emit(self, img):
        self.OriCamlabel.setPixmap(QPixmap.fromImage(img))

    def openCV_emit(self,img):
        self.ProcessedCamlabel.setPixmap(QPixmap.fromImage(img))
    
    def Capture_emit(self,img):
        self.ProcessedCapturedLabel.setPixmap(QPixmap.fromImage(img))

    def openCV_stop_emit(self):
        img = QImage()
        self.OriCamlabel.setPixmap(QPixmap.fromImage(img))
        self.ProcessedCamlabel.setPixmap(QPixmap.fromImage(img))
        self.ProcessedCapturedLabel.setPixmap(QPixmap.fromImage(img))


    def about_sftwr(self):
        QMessageBox.information(self, "Software Version", 
                                      "You are running on the latest version V1.0.0",
                                      QMessageBox.Ok)

    def quit_app(self):
        sys.exit(0)
