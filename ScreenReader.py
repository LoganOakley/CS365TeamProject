import cv2
import numpy as np
import win32gui
import win32ui
import win32con   # pip install pywin32
import ctypes  # allows GetSystemMetrics
from datetime import datetime
import time
from ImageProcessing import *


class Counter:
    def __init__(self):
        self.start_time = None
        self.occurrence_count = 0

    def start(self):
        self.start_time = datetime.now()
        return self

    def increment(self):
        self.occurrence_count += 1

    def countPerSec(self):
        time_elapsed = (datetime.now() - self.start_time).total_seconds()
        return round(self.occurrence_count / time_elapsed, 2)


class NewWindowCapture:
    windowhandle = None
    width = 0
    height = 0
    # change
    cropped_x = 0
    cropped_y = 0
    offset_x = 0
    offset_y = 0
    #stores a function that does the desired processing. 
    processing_type = None

    
    # constructor
    def __init__(self, window):
        self.windowhandle = win32gui.FindWindow(None, window)
        if not self.windowhandle:
            raise Exception(f'Window does not exist: {format(window)}')

        window_size = win32gui.GetWindowRect(self.windowhandle)
        self.width = window_size[2] - window_size[0]
        self.height = window_size[3] - window_size[1]

        # cut out titlebar
        border_pixels = 8
        titlebar_pixels = 30
        self.width = self.width - (border_pixels * 2)
        self.height = self.height - titlebar_pixels - border_pixels
        self.cropped_x = border_pixels
        self.cropped_y = titlebar_pixels

        self.offset_x = window_size[0] + self.cropped_x
        self.offset_y = window_size[1] + self.cropped_y

    def grab_screenshot(self):

        windowDeviceContext = win32gui.GetWindowDC(self.windowhandle)
        createdDeviceContext = win32ui.CreateDCFromHandle(windowDeviceContext)
        compatibleContext = createdDeviceContext.CreateCompatibleDC()
        bmpData = win32ui.CreateBitmap()
        bmpData.CreateCompatibleBitmap(createdDeviceContext, self.width, self.height)
        compatibleContext.SelectObject(bmpData)
        compatibleContext.BitBlt((0, 0), (self.width, self.height), createdDeviceContext,
                                 (self.cropped_x, self.cropped_y), win32con.SRCCOPY)

        signedArray = bmpData.GetBitmapBits(True)
        img = np.fromstring(signedArray, dtype='uint8')
        img.shape = (self.height, self.width, 4)

        createdDeviceContext.DeleteDC()
        compatibleContext.DeleteDC()
        win32gui.ReleaseDC(self.windowhandle, windowDeviceContext)
        win32gui.DeleteObject(bmpData.GetHandle())

        # drop the alpha channel, or cv2.matchTemplate() will throw an error like:
        #   error: (-215:Assertion failed) (depth == cv2_8U || depth == cv2_32F) && type == _templ.type()
        #   && _img.dims() <= 2 in function 'cv2::matchTemplate'
        img = img[..., :3]
        self.processing_type = detectEdges
        return self.process_image(img)

    #create psuedo delegate so that we can change the processing being performed by changing the attr processing_type
    def process_image(self, img):
        return self.processing_type(img)

    def get_screen_position(self, pos):
        return (pos[0] + self.offset_x, pos[1] + self.offset_y)
