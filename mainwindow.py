import sys, serial, threading
import serial.tools.list_ports
import cv2
import numpy as np
import mvsdk
import os, re, time
from threading import Thread, Event
from PySide6.QtGui import QImage, QPixmap, QPainter,QBrush, QColor
from PySide6.QtCore import QCoreApplication, QThread, QPoint, QRect, Signal, Slot
from PySide6.QtWidgets import QMainWindow, QWidget, QMessageBox
from PySide6.QtMultimedia import QMediaDevices
from SDKtool import Camera
from ui_Main import Ui_MainWindow 
from ui_ROIwidget import Ui_ROIWidget  
from labelimage import Labelimage  
from hold_button import HoldButton   
       

class CameraProcess(QThread):
    #Pembuatan sinyal untuk passing nilai variabel dari working thread ke GUI (variabel hasil dari process pada thread)
    Image=Signal(QImage)
    ImageProcess = Signal(QImage)
    ImageCaptured = Signal(QImage)
    ImageROI = Signal(QImage)
    RGBgain = Signal(int,int,int)
    ObjCondition = Signal(str)

    Xoff = 0
    Yoff = 0
    Width = 0
    Height = 0
    condition = ""

    def run(self):
        #global instance (untuk keperluan nilai yang dapat diakses fungsi manapun)
        global camIndex, camState
        global InspectState
        global ExpState
        global exp, fg, wb
        global iR, iG, iB
        
        global update
        global status
        global chg
        global setROI
        global boundUpdate

        boundUpdate = False
        
        setROI = False
        update = False

        ExpState= "Auto"
        i = 0
        #Kondisi untuk menentukan penggunaan kamera dari sistem atau machine vision camera
        #If sistem kamera (built in webcam / external webcam)
        if camState == "SYS":
            self.capture = cv2.VideoCapture(0)
            self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
            self.capture.set(cv2.CAP_PROP_FRAME_WIDTH,640)
        
        #Else if Machine Vision camera (HuaTeng/MindVision/etc.)
        elif camState == "MV":
            self.capture = Camera(DeviceList.DevList[camIndex])

            #Check if opened (ambil parameter dari kelas 'Camera')
            if self.capture.open():
                self.hCamera = self.capture.camer()                
                print(self.capture)
                
        self.ThreadActive = True

        #Infinite loop (agar thread selalu berjalan dalam sekali panggilan)
        while self.ThreadActive:

            #inisiasi frame capture (tidak terlalu dikembangkan untuk sekarang)
            if camState == "SYS":
                ret, frame = self.capture.read()
                frame = cv2.flip(src=frame, flipCode=1)

            #inisiasi frame capture dengan Machine Vision Camera
            elif camState == "MV":
                #fungsi untuk menyesuaikan exposure setting dan gain analog secara real-time
                self.capture.setExp(ExpState, exp, fg)

                #Update Resolution size ke display
                if update == True:
                    self.capture.setROI(CameraProcess.Xoff, CameraProcess.Yoff, CameraProcess.Width, CameraProcess.Height)
                    update = False

                #Auto White Balance, ambil nilai channel hasil white balance dan passing ke variable pada GUI
                if wb == True:
                    iR, iG, iB = self.capture.setWhiteBalance()
                    self.RGBgain.emit(iR,iG,iB)
                    
                #Independent color Gain (tanpa balancing warna)
                if wb == False:
                    mvsdk.CameraSetGain(self.hCamera, iR, iG, iB)

                #Pengambilan frame dengan fungsi .grab() dan resize agar muat pada kolom GUI
                frame = self.capture.grab()
                self.pBuffer, self.fHead = self.capture.ReturnPHead()
                frame = cv2.resize(frame, (640, 480), interpolation= cv2.INTER_LINEAR)
                
            #Process for image processing step (Post-processing)
            if frame is not None:
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                height, width, channel = frame_rgb.shape
                q_img = QImage(frame_rgb.data, width, height, width * channel, QImage.Format_RGB888) #variable for actual image in window 1

                #initial capture for ROI image (one time run)
                if i == 0:
                    r_img = q_img #variable of reference image for first run
                    i = 1

                #self processing frame
                if InspectState == 0:
                    p_img = q_img #variable for processing algorithm in window 2
                    s_img = QImage() #variable of captured frame in window 3

                #If Inspect button clicked, assign the frame to Image Processing function (Auto Mode)
                elif InspectState == 1:
                    p_img = self.ProcessImage(frame) #pakai variable p_img untuk menampilkan frame copy yang di proses
                    
                    #Check if arduino has finished its motion, and return the captured image
                    if status == "show":
                        s_img = p_img
                        self.ObjCondition.emit(self.condition)
                        status = "wait"
                
                    elif status == "wait":
                        pass
                    
                    else: s_img = QImage()
                #Function to call when set ROI button clicked (berhubungan dengan Qwidget set ROI)
                if setROI == True:
                    self.ImageROI.emit(r_img) #pakai variabel r_img untuk reference image by default
                    setROI = False          

                #Self capturing frame
                self.Image.emit(q_img)
                self.ImageProcess.emit(p_img)
                self.ImageCaptured.emit(s_img)
        
        self.capture.close()

    def stop(self):
        self.ThreadActive = False
        self.quit()

    def ProcessImage(self, frame):
        global GrayCB, NoRedCB, HistCB, roiCB, TmpMatCB, BlobCB
        global boundUpdate, InspectState

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply noise reduction (Gaussian blur)
        blurred_frame = cv2.GaussianBlur(gray_frame, (9, 9), 0)

        # Apply Contrast limit Adaptive histogram equalization
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        equalized_frame = clahe.apply(blurred_frame)

        # Perform ROI extraction
        # Define region of interest (ROI) coordinates
        if boundUpdate == False:
            roi_x, roi_y, roi_width, roi_height = 252, 180, 104, 114
        
        if boundUpdate == True:
            roi_x, roi_y, roi_width, roi_height = 0, 0, 640, 480

        roi = equalized_frame[roi_y:roi_y + roi_height, roi_x:roi_x + roi_width]

        # Perform blob analysis
        _, thresholded_roi = cv2.threshold(roi, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        contours, _ = cv2.findContours(thresholded_roi, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Draw ROI rectangle on the original frame
        frame_with_contours = frame.copy()

        if InspectState != 0:
            cv2.rectangle(frame_with_contours, (roi_x, roi_y), (roi_x + roi_width, roi_y + roi_height), (0, 255, 0), 2)

            # Draw contours within the ROI
            for contour in contours:
                area = cv2.contourArea(contour)
                # Perimeter
                perimeter = cv2.arcLength(contour, True)
                # Convex hull area and solidity

                
                if len(contour) >= 5:  # FitEllipse needs at least 5 points
                    ellipse = cv2.fitEllipse(contour)
                    (center, axes, orientation) = ellipse
                    majoraxis_length = max(axes)
                    minoraxis_length = min(axes)
                    eccentricity = np.sqrt(1 - (minoraxis_length / majoraxis_length) ** 2)
                else:
                    eccentricity = 0

                # Define defect criteria (example: area too large or too small)
                if area > 136 or perimeter > 100 or eccentricity > 0.7:
                    contour += (roi_x, roi_y)  # Shift contour coordinates to match ROI position
                    cv2.drawContours(frame_with_contours, [contour], -1, (0, 0, 255), 2)
                    cv2.putText(frame_with_contours, "Defect", (roi_x, roi_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
                    self.condition = "STATUS: DEFECT"
        '''        
        # gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # # Apply noise reduction (Gaussian blur)
        # blurred_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)

        # # Apply Contrast limit Adaptive histogram equalization
        # clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        # equalized_frame = clahe.apply(blurred_frame)

        # # Perform ROI extraction
        # # Define region of interest (ROI) coordinates
        # roi_x, roi_y, roi_width, roi_height = 100, 100, 200, 200
        # roi = equalized_frame[roi_y:roi_y + roi_height, roi_x:roi_x + roi_width]

        # # Perform blob analysis
        # _, thresholded_roi = cv2.threshold(roi, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        # contours, _ = cv2.findContours(thresholded_roi, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # # Draw ROI rectangle on the original frame
        # frame_with_contours = frame.copy()
        # cv2.rectangle(frame_with_contours, (roi_x, roi_y), (roi_x + roi_width, roi_y + roi_height), (0, 255, 0), 2)

        # # Draw contours within the ROI
        # for contour in contours:
        #     contour += (roi_x, roi_y)  # Shift contour coordinates to match ROI position
        #     cv2.drawContours(frame_with_contours, [contour], -1, (0, 0, 255), 2)

        # Convert processed frame back to QImage'''
        height, width, channel = frame_with_contours.shape
        bytes_per_line = 3 * width
        q_img_prc = QImage(frame_with_contours.data, width, height, bytes_per_line, QImage.Format_BGR888)
        
        if InspectState == 0:
            return None
        
        return q_img_prc

    def SaveIMG (self, i):
        mvsdk.CameraFlipFrameBuffer(self.pBuffer, self.fHead, 1)
        mvsdk.CameraSaveImage(self.hCamera, "./SampleData/Sample_Data{}.bmp".format(i), self.pBuffer, self.fHead, mvsdk.FILE_BMP, 100)
        print("Sample_Data{} is saved".format(i))

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

class AnotherWidget(QWidget, Ui_ROIWidget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Custom ROI selection")
        self.imgLabel = Labelimage(self)
           
        self.imgLabel.roi_selected.connect(self.whenROIselected)
        self.SetImgButton.clicked.connect(self.setfixROI)

    @Slot()
    def show_image(self,image):
        self.ShowImage.setPixmap(QPixmap.fromImage(image))
    
    def whenROIselected(self, bool):
        if bool == True:           
            self.lineXofst.setText(str(self.imgLabel.X))
            self.lineYofst.setText(str(self.imgLabel.Y))
            self.lineFocusW.setText(str(self.imgLabel.WIDTH))
            self.lineFocusH.setText(str(self.imgLabel.HEIGHT))

            CameraProcess.Xoff, CameraProcess.Yoff, CameraProcess.Width, CameraProcess.Height = self.imgLabel.X, self.imgLabel.Y, self.imgLabel.WIDTH, self.imgLabel.HEIGHT
            print( CameraProcess.Xoff, CameraProcess.Yoff, CameraProcess.Width, CameraProcess.Height)

    def setfixROI(self):
            global update
            update = True

class mainWindow(QMainWindow, Ui_MainWindow):
    s = 0
    i = 1
        
    def __init__(self):
        global camIndex, wb, chg
        global iR, iG, iB
        global InspectState
        iR =  100
        iG = 100
        iB = 100

        chg = True
        wb = False

        InspectState = 0

        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Recorder Inspection Monitor V1.0")
        self.resize(1280,800)

        self.ROIwindow = AnotherWidget()
        
        #Set-up Menubar function
        self.actionAbout_Software.triggered.connect(self.about_sftwr)
        self.actionQuit.triggered.connect(self.quit_app)
        self.actionCamera.triggered.connect(self.quitCameraThread)
        self.actionArduino.triggered.connect(self.quitArduinoThread)
        self.actionAll.triggered.connect(self.quitAllThread)
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
        self.StoppButton.holdPressed.connect(self.onHold_Rotate)
        self.StoppButton.holdReleased.connect(self.onHold_Release)
        
        self.mode = 0
        self.command = ""
        
        self.UpdateBoundButton.clicked.connect(self.UpdateSetting)
        self.AWBButton.clicked.connect(self.AutoWb)

        self.SaveImgButton.clicked.connect(self.saveImage)

        self.spinBoxRW.valueChanged.connect(self.setResWidth)
        self.spinBoxRH.valueChanged.connect(self.setResHeight)

        self.setROIButton.clicked.connect(self.toggle_roiWindow)
        self.ROIwindow.RefreshImgButton.clicked.connect(self.toggle_roiWindow)

        self.expSlider.valueChanged.connect(self.setExpTime)
        self.gainSlider.valueChanged.connect(self.setAnGain)

        if chg == True:
            self.RGainSlider.setValue(iR)
            self.GGainSlider.setValue(iG)
            self.BGainSlider.setValue(iB)
            chg = False
        
        self.RGainSlider.valueChanged.connect(self.setRGain)
        self.GGainSlider.valueChanged.connect(self.setGGain)
        self.BGainSlider.valueChanged.connect(self.setBGain)

        self.GRcheck.checkStateChanged.connect(self.Feature_selector)
        self.NRcheck.checkStateChanged.connect(self.Feature_selector)
        self.Histocheck.checkStateChanged.connect(self.Feature_selector)
        self.REcheck.checkStateChanged.connect(self.Feature_selector)
        self.TMcheck.checkStateChanged.connect(self.Feature_selector)
        self.IDcheck.checkStateChanged.connect(self.Feature_selector)
        self.BAcheck.checkStateChanged.connect(self.Feature_selector)
        
        self.AutoExpButton.toggle()
        self.AutoExpButton.toggled.connect(self.ExpMode)
        self.ManualExpButton.toggled.connect(self.ExpMode)

        #Setup Initial widget state
        self.expSlider.setRange(1,130)
        self.gainSlider.setRange(5,33)
        self.spinBoxRW.setRange(0,1280)
        self.spinBoxRH.setRange(0,1024)

        self.RGainSlider.setRange(0,399)
        self.GGainSlider.setRange(0,399)
        self.BGainSlider.setRange(0,399)

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
        
    #========== Camera Related Function Definition ============#

    def saveImage(self): #Fungsi GUI untuk Menyimpan gambar ke Folder
        files = os.listdir("./SampleData")
    
        # Filter files matching the base_name and extension pattern
        pattern = re.compile(rf"Sample_Data(\d+)\.bmp$")
        matching_files = [f for f in files if pattern.match(f)]
        
        # Extract the numerical part from the filenames
        numbers = [int(pattern.match(f).group(1)) for f in matching_files]
        
        # Determine the highest number
        if numbers:
            next_number = max(numbers) + 1
        else:
            next_number = 0  # Start from 0 if no files found

        # Generate the new filename
        self.Worker1_Opencv.SaveIMG(next_number)

    def toggle_roiWindow(self): #Fungsi GUI ntuk menampilkan window ROI setting
        global setROI

        setROI = True

        if not self.ROIwindow.isVisible():
            self.ROIwindow.show()
        
        self.Worker1_Opencv.ImageROI.connect(self.ROIwindow.show_image)
        print("The image should've shown")

    def AutoWb(self): #Fungsi untuk set-up Auto White balance
        global wb
        wb = True

        self.Worker1_Opencv.RGBgain.connect(self.setRGBGpos) #slot untuk mengambil sinyal nilai gain color channel dari thread kamera

    def setRGBGpos(self, iR, iG,iB): #Fungsi yang digunakan untuk mengatur posisi slider sesuai nilai sinyal variabel gain dari thread Camera
        self.RGainSlider.setSliderPosition(iR) #Merah
        self.GGainSlider.setSliderPosition(iG) #Hijau
        self.BGainSlider.setSliderPosition(iB) #Biru

    def UpdateSetting(self): 
        global boundUpdate
        boundUpdate = True
    
    def setResWidth(self):
        global Width
        self.Worker1_Opencv.Width = self.spinBoxRW.value()

    def setResHeight(self):
        global Height
        self.Worker1_Opencv.Height = self.spinBoxRH.value()

    def setExpTime(self): #Fungsi untuk mengatur lamanya bukaan sensor pada mode manual exposure
        global exp
        exp = self.expSlider.value()*1000 #nilai satuannya dalam unit microsecond, sehingga * 1000 untuk mendapatkan ms
    
    def setAnGain(self): #Fungsi untuk mengatur gain atau sensitivitas kecerahan pada sensor kamera (manual exposure)
        global fg
        fg = self.gainSlider.value()

    def setRGain(self): #Fungsi untuk mengambil nilai pengaturan channel merah pada gambar
        global iR, wb 
        wb = False
        iR = self.RGainSlider.value()

    def setGGain(self): #Fungsi untuk mengambil nilai pengaturan channel hijau pada gambar
        global iG, wb
        wb = False
        iG = self.GGainSlider.value()
    
    def setBGain(self): #Fungsi untuk mengambil nilai pengaturan channel biru pada gambar
        global iB, wb
        wb = False
        iB = self.BGainSlider.value()

    def showOKbutton(self): #Fungsi GUI yang mengatur logic jika COM port dan Camera Device telah dipilih
        if self.s==1:
            self.OkButton.setEnabled(True)
        else:
            self.s+=1

    def Auto_Mode(self): #Fungsi GUI untuk memilih mode inspeksi otomatis
        global status, InspectState
        
        InspectState = 0
        status = ""
        self.mode = 0

        self.CameraON() #Pemanggilan fungsi untuk memulai thread camera
        self.groupBox_3.setDisabled(True)
        self.groupBox_5.setDisabled(True)
        self.ManualButton.setDisabled(False)
        self.AutoButton.setDisabled(True)
        self.InspectButton.setDisabled(False)

    def Manual_Mode(self): #Fungsi GUI untuk memilih mode inspeksi secara manual (belum dikembangkan lebih lanjut)
        global status, InspectState, arm
        
        InspectState = 0
        status = ""
        self.mode = 1
        self.j = 0
        arm = ""

        self.ManualButton.setDisabled(True)
        self.StartButton.setDisabled(False)
        self.StopButton.setDisabled(False)

        self.InspectButton.setText("GRIP")
        self.StoppButton.setText("ROTATE")
        self.InspectButton.setDisabled(False)
        self.StoppButton.setDisabled(False)

    def Inspect(self): #Fungsi untuk menjalankan mode inspeksinya
        global status, InspectState
        global arm, Port

        if self.mode == 0: #Mode Otomatis
            try:
                InspectState = 1 #pengaturan global variabel ini untuk memberi sinyal pada thread agar menampilkan frame post processing

                if Port.is_open:
                #Arduino command, untuk menjalankan thread Arduino untuk memutar komponen
                    self.Worker2_Arduino = Thread(target=self.ArduinoCOM)
                    self.stop_thread = False
                    self.Worker2_Arduino.start()

                elif not Port.is_open:
                    Port.open()
                    self.Worker2_Arduino = Thread(target=self.ArduinoCOM)
                    self.stop_thread = False
                    self.Worker2_Arduino.start()


            except:
                return "Error"
        
        
        elif self.mode == 1: #Mode Manual
            
            try:
                if self.InspectButton.text() == "UNGRIP" and self.j==1:
                    arm = "UNGRIP"
                    self.j = 2
                    self.InspectButton.setText("GRIP")

                elif self.InspectButton.text() == "GRIP" and self.j==0 or self.j==3:
                    arm = "GRIP"
                    self.j = 1
                    self.InspectButton.setText("UNGRIP")

                else:
                    self.j += 1

            except:
                return "Error"

        
    def ExpMode(self): #Pengaturan mode exposure pada kamera
        global ExpState

        if self.AutoExpButton.isChecked():
            ExpState = "Auto"
        
        elif self.ManualExpButton.isChecked():
            ExpState = "Manual"

    def Feature_selector(self): #Pengaturan jenis post porcessing yang ingin dijalankan pada thread Camera
        global GrayCB, NoRedCB, HistCB, roiCB, TmpMatCB, IDeffCB, BlobCB

        if self.GRcheck.isChecked() == True:
            GrayCB = True
        elif self.GRcheck.isChecked() == False:
            GrayCB = False
        
        if self.NRcheck.isChecked() == True:
            NoRedCB = True
        elif self.NRcheck.isChecked() == False:
            NoRedCB = False

        if self.Histocheck.isChecked() == True:
            HistCB = True
        elif self.Histocheck.isChecked() == False:
            HistCB = False

        if self.REcheck.isChecked() == True:
            roiCB = True
        elif self.REcheck.isChecked() == False:
            roiCB = False

        if self.TMcheck.isChecked() == True:
            TmpMatCB = True
        elif self.TMcheck.isChecked() == False:
            TmpMatCB = False

        if self.IDcheck.isChecked() == True:
            IDeffCB = True
        elif self.IDcheck.isChecked() == False:
            IDeffCB = False

        if self.BAcheck.isChecked() == True:
            BlobCB = True
        elif self.BAcheck.isChecked() == False:
            BlobCB = False

    def CameraON (self): #Inisiasi worker thread yang berisi kelas Camera()
        self.Worker1_Opencv = CameraProcess()
        self.Worker1_Opencv.Image.connect(self.cam_emit)
        self.Worker1_Opencv.ImageProcess.connect(self.openCV_emit)
        self.Worker1_Opencv.ImageCaptured.connect(self.Capture_emit)

        self.Worker1_Opencv.ObjCondition.connect(self.SetStatsLabel)
        
        self.Worker1_Opencv.start()

    def submitCOMcam(self): #Fungsi untuk memvalidasi pilihan COM Port dan Camera Device
        mainWindow.s = 0
        global camIndex, camState, Port

        #COM Port connection
        Port = ComPort.serialInst
        Portnum = self.ComboPort.currentText()
        match = re.search(r'COM\d+', Portnum)
        if match:
            Port.port = 'COM9' #match.group(0)
            Port.baudrate = 9600
        
        try:
            Port.open()
            Port.write('Opening COM Test Message'.encode('utf-8'))
            self.hold = False

        except SyntaxError as e:
            return e.msg

        #Device & Camera connection
        camText = self.ComboCam.currentText()
        
        if camText in DeviceList.CamList: #Apabila yang dipilih sistem kamera
            camState = "SYS"
            camIndex = self.ComboCam.currentIndex()
            if camIndex == 0: camIndex +=1
            elif camIndex == 1: camIndex -=1
            
            print("Connected to Camera from System")

        elif camText in DeviceList.hlist: #Apabila yang dipilih adalah kamera machine vision
            camState = "MV"
            camIndex = DeviceList.hlist.index(camText)
            print("Connected to MV Camera")

        self.OkButton.setDisabled(True)
        self.AutoButton.setDisabled(False)
        self.ManualButton.setDisabled(False)
        self.PORTDEV_connected()

    
    def ArduinoCOM(self):
        global status, InspectState, arm, Port
        
        if self.mode == 0:
            self.n = 0
            self.command = "GRIP"
            try:
                while not self.stop_thread:
                    while Port.in_waiting == 0 and not self.stop_thread:
                        if self.command in ["GRIP", "RTT", "FRTT", "UNGRIP"]:
                            Port.write(self.command.encode('utf-8'))
                            # print(self.command)
                            self.command = ""
                    if self.stop_thread:
                        break

                    r_packet = Port.readline().decode('utf-8').strip('\r\n')

                    if r_packet == "FINISH GRIP" :
                        print(r_packet)
                        status = "show"
                        self.saveImage()
                        self.command = "FRTT"

                    if r_packet == "FINISH ROTATE":
                        print(r_packet)
                        status = "show"
                        self.saveImage()
                        self.command = "FRTT"
                        self.n += 1

                    if r_packet == "FINISH ROTATE" and self.n == 4:
                        print("Arduino Finish rotation, please change sample")
                        self.command = "UNGRIP"
            except:
                return Exception
            
        elif self.mode == 1:  # Manual Mode
            while not self.stop_thread:
                while Port.in_waiting == 0 and not self.stop_thread:
                    self.command=arm
                    if self.command in ["GRIP", "RTT", "UNGRIP"]:
                        Port.write(self.command.encode('utf-8'))
                        arm = ""
                        self.command = ""
                if self.stop_thread:
                    break
                r_packet = Port.readline().decode('utf-8').strip('\r\n')

                if r_packet == "FINISH GRIP":
                    print(r_packet)
                    status = "show"

                if r_packet == "FINISH ROTATE":
                    print(r_packet)
                    status = "show"

        Port.close()
    
    def onHold_Rotate(self):
        if self.mode == 1:
            self.hold = True
        else: 
            pass
    
    def onHold_Release(self):
        if self.mode == 1:
            global arm
            arm = "FRTT"

            
    def SetStatsLabel(self, status):
        self.statsLabel.setText(status)

    def Auto_Mode_stop(self):
        global arm

        if self.mode == 0:
            self.StoppButton.setDisabled(True)
            self.InspectButton.setDisabled(False)
            self.statsLabel.setText("STATUS: Stopping")
            
            try:
                self.quitArduinoThread()
                InspectState = 0
            
            except TypeError as e:
                return e
            
            self.statsLabel.setText("STATUS:")

        if self.mode == 1:

            try:
                if self.InspectButton.text() == "UNGRIP":
                    if self.hold==True:
                        arm = "FRTT"
                        print(arm)
                        self.hold=False
                    else:
                        arm = "RTT"
                        self.j += 1

            except:
                return "Error"
        
    def StartCam(self):
        global InspectState, arm, Port

        InspectState = 1

        self.StartButton.setDisabled(True)
        self.StopButton.setDisabled(False) 
        self.CameraON()
        arm = ""
        if Port.is_open:
        #Arduino command, untuk menjalankan thread Arduino untuk memutar komponen
            print ("Port Already Open")
            self.Worker2_Arduino = Thread(target=self.ArduinoCOM)
            self.stop_thread = False
            self.Worker2_Arduino.start()

        else:
            Port.open()
            self.Worker2_Arduino = Thread(target=self.ArduinoCOM)
            self.stop_thread = False
            self.Worker2_Arduino.start()

        
    def StopCam(self):
        self.StopButton.setDisabled(True)
        self.StartButton.setDisabled(False)
        self.quitCameraThread()
    
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
        self.AutoButton.setEnabled(True)


    def about_sftwr(self):
        QMessageBox.information(self, "Software Version", 
                                      "You are running on the latest version V1.0.0",
                                      QMessageBox.Ok)

    def PORTDEV_connected(self):
        QMessageBox.information(self, "Serial port and Camera device connected successfully",
                                    "PORT:{} \nCAM: {}".format(self.ComboPort.currentText(), self.ComboCam.currentText()), 
                                    QMessageBox.Ok)
    def quit_app(self):
        self.quitArduinoThread()
        self.quitCameraThread()
        sys.exit(0)
    
    def quitArduinoThread(self):
        global InspectState
        
        if InspectState == 1 :
            self.stop_thread = True
            self.Worker2_Arduino.join()
        
        else: pass

    def quitCameraThread(self):
        if hasattr(self, 'Worker1_Opencv') and isinstance(self.Worker1_Opencv, CameraProcess):
            if self.Worker1_Opencv.isRunning():
                self.Worker1_Opencv.stop()
                self.Worker1_Opencv.quit()
                self.Worker1_Opencv.wait()
                self.openCV_stop_emit()

        else:
            pass

    def quitAllThread(self):
        self.quitArduinoThread()
        self.quitCameraThread()

    def closeEvent(self, event):
        self.quit_app()  # Ensure thread is stopped when closing the window
        event.accept()