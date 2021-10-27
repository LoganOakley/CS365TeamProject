from ScreenReader import NewWindowCapture, Counter
import numpy as np
import cv2
import os
from datetime import datetime
import time
import win32gui
import win32ui
import win32con  # pip install pywin32
import ctypes  # allows GetSystemMetrics


def main():

    def process_img(original_image):

        processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

        processed_img = cv2.Canny(processed_img, threshold1=50, threshold2=100)

        return processed_img

    wincap = NewWindowCapture('Stella 6.5.3: "Asteroids (1981) (Atari)"')

    myCounter = Counter()
    myCounter.start()
    while(True):
        screenshot = wincap.grab_screenshot()
        cv2.imshow('Computer Vision', screenshot)

        print(myCounter.countPerSec())
        myCounter.increment()

        if cv2.waitKey(1) == ord('q'):
            cv2.destroyAllWindows()
            break

    print('Finished')


if __name__ == "__main__":
    main()
