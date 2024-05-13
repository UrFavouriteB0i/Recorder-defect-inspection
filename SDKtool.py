import cv2
import numpy as np
import mvsdk
import platform

class Camera(object):
    def __init__(self, DevInfo):
        super(Camera, self).__init__()
        self.DevInfo = DevInfo
        self.hCamera = 0 
        self.cap = None
        self.pFrameBuffer = 0

    def open(self):
        if self.hCamera > 0:
            return True
        
        #Turning On the Camera
        hCamera = 0
        try:
            hCamera = mvsdk.CameraInit(self.DevInfo, -1, -1)
        except mvsdk.CameraException as e:
            print("CameraInit Failed ({}): {}".format(e.error_code, e.message))

        #Get Camera Feature description
        cap = mvsdk.CameraGetCapability(hCamera)
        
        #set up as color camera
        mvsdk.CameraSetIspOutFormat(hCamera, mvsdk.CAMERA_MEDIA_TYPE_BGR8)

        #Calculate required size for RGB Buffer which allocated directly as max res of the camera
        FrameBufferSize = cap.sResolutionRange.iWidthMax * cap.sResolutionRange.iHeightMax * 3

        #Allocate the RGB Buffer to store image output by ISP
        #Note:RAW data is transmitted from the camera to the PC, 
        #and converted to RGB data through the software ISP on the PC 
        #(if it is a black and white camera, there is no need to convert the format, 
        #but the ISP has other processing, so this buffer also needs to be allocated)
        pFrameBuffer = mvsdk.CameraAlignMalloc(FrameBufferSize,16)

        #Switch camera mode to continuous acquisition
        mvsdk.CameraSetTriggerMode(hCamera, 0)

        #Also set Manual exposure, exposure time 30ms
        mvsdk.CameraSetAeState(hCamera, 0)
        mvsdk.CameraSetExposureTime(hCamera, 30*1000)
        
        #Let the SDK internal image taking thread start working
        mvsdk.CameraPlay(hCamera)

        self.hCamera = hCamera
        self.pFrameBuffer = pFrameBuffer
        self.cap = cap
        return True
    
    def close(self):
        if self.hCamera > 0: 
            mvsdk.CameraUnInit(self.hCamera)
            self.hCamera = 0
        
        mvsdk.CameraAlignFree(self.pFrameBuffer)
        self.pFrameBuffer = 0

    def grab(self): 
        #Get a frame from the camera
        hCamera = self.hCamera
        pFrameBuffer = self.pFrameBuffer

        try:
            pRawData, FrameHead = mvsdk.CameraGetImageBuffer(hCamera,200)
            mvsdk.CameraImageProcess(hCamera, pRawData, pFrameBuffer, FrameHead)
            mvsdk.CameraReleaseImageBuffer(hCamera, pRawData)

            #The image data obtained under Windows is upside down and stored in BMP format. 
            #To convert to opencv, you need to flip it up and down to be positive.
            mvsdk.CameraFlipFrameBuffer(pFrameBuffer, FrameHead, 1)

            #At this time, the picture has been stored in pFrameBuffer. 
            #For color cameras, pFrameBuffer=RGB data, and 
            #for black and white cameras, pFrameBuffer=8-bit grayscale data.
            # Convert pFrameBuffer to opencv image format for subsequent algorithm processing
            frame_data = (mvsdk.c_ubyte * FrameHead.uBytes).from_address(pFrameBuffer)
            frame = np.frombuffer(frame_data, dtype=np.uint8)
            frame = frame.reshape((FrameHead.iHeight, FrameHead.iWidth, 3))
            return frame
        
        except mvsdk.CameraException as e:
            if e.error_code != mvsdk.CAMERA_STATUS_TIME_OUT:
                print("CameraGetImageBuffer failed({}): {}".format(e.error_code, e.message))
            return None