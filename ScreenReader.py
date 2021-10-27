import numpy as np

from PIL import ImageGrab

import cv2

import win32gui as wg
import win32ui as wu
import win32con as wc  # pip install pywin32

import ctypes  # allows GetSystemMetrics
import re
import multiprocessing
from datetime import datetime
import time

# should allow us to grab framerate


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


class WindowCapture:

    # getting user's desktop size to properly calculate game window

    user = ctypes.windll.user32

    w = user.GetSystemMetrics(0)

    h = user.GetSystemMetrics(1)

    print(f"Width is {w}")  # for testing

    print(f"Height is {h}")  # for testing

    # Detects Stella Window, perhaps we can define rom file names and pass those as variables with Stella 6.5.3 + whatever game rom

    wind = wg.FindWindow(None, 'Stella 6.5.3')

    # analyze window

    rect = wg.GetWindowRect(wind)


def process_img(original_image):

    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

    processed_img = cv2.Canny(processed_img, threshold1=50, threshold2=100)

    return processed_img


def displaywindow():
    myCounter = Counter()
    myCounter.start()
    while(True):

        mainwin = WindowCapture()
        #screen = np.array(ImageGrab.grab(bbox=(0, 40, 800, 640)))
        screen = np.array(ImageGrab.grab(
            bbox=(mainwin.rect[0], mainwin.rect[1], mainwin.rect[2], mainwin.rect[3])))
        new_screen = process_img(screen)
        #printscreen_numpy = cv2.cvtColor(screen,cv2.COLOR_BGR2RGB)
        cv2.imshow('window', new_screen)
        if cv2.waitKey(25) & 0xFF == ord('q'):

            cv2.destroyAllWindows()

            break
        print(myCounter.countPerSec())
        myCounter.increment()


t1 = multiprocessing.Process(target=displaywindow())
t2 = multiprocessing.Process(target=displaywindow())
t3 = multiprocessing.Process(target=displaywindow())

t1.start()
t2.start()
t3.start()
