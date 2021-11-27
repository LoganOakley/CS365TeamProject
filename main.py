from Controller import GoLeft, Shoot, Start, bringToFront
from ScreenReader import NewWindowCapture, Counter
import numpy as np
from ImageProcessing import *
import cv2
import os
from datetime import datetime
import time
import win32gui
import win32ui
import win32con  # pip install pywin32
import ctypes
from Tracking import drawBoxes
from game import *
from threading import Thread

def main(gamename = 'No Name'):

    game = gamename

    def FindWindowEnum(hwnd, ctx):
        windowstring = win32gui.GetWindowText(hwnd)
        if 'Stella' in windowstring:
            bringToFront()
            wincap = NewWindowCapture(windowstring)
            wincap.change_processing(noFilter)
            myCounter = Counter()
            myCounter.start()
            en1 = cv2.imread('resources/MatchTemplateImages/enemy1.png', cv2.COLOR_BGR2GRAY)
            en2 = cv2.imread('resources/MatchTemplateImages/enemy2.png', cv2.COLOR_BGR2GRAY)
            spider = cv2.imread('resources/MatchTemplateImages/spider.png', cv2.COLOR_BGR2GRAY)
            Start()
            while(True):
                screenshot = wincap.grab_screenshot()
                screenshot = drawBoxes(screenshot,spider)
                cv2.imshow('Computer Vision', screenshot)
                count = myCounter.countPerSec()
                print(count)
                myCounter.increment()
                
                GoLeft()
                Shoot()
                key = cv2.waitKey(3)
                if key == ord('q'):
                    cv2.destroyAllWindows()
                    break
                #for purposes of positive cascade images
                #elif key == ord('f'):
                  #  cv2.imwrite(f'resources/CascadeClassifier/Centipede/Positive/{str(count)}.jpg', screenshot)
                   # print('Hello')
                    

            print('Finished')

    findwindow = win32gui.EnumWindows(FindWindowEnum, None)
    # Goes through all windows and does the loop when the window name contains our chosen string


if __name__ == "__main__":
    main()
