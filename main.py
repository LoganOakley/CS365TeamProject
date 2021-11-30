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
from Tracking import *
from game import *
from threading import Thread
import math

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
            spider = cv2.imread('resources/MatchTemplateImages/spider1.png')
            enMiddle = cv2.imread('resources/MatchTemplateImages/enemyMiddle.png')
            player = cv2.imread('resources/MatchTemplateImages/PlayerSprite.png')
            
            Start()
            while(True):
                screenshot = wincap.grab_screenshot()
                ROI = screenshot[0:math.ceil(wincap.height * .85), math.ceil(wincap.width * .08):math.ceil(wincap.width*.92)]
                #ROI = screenshot[0:410,0:600] Quaid Note, this incorrectly sizes my stella window
                view = getLocations(ROI,player,'player')
                view = view + getLocations(ROI, enMiddle, 'enemy')
                view = view + getLocations(ROI, spider, 'spider', .75)
                #view = view + drawBoxes(ROI, en2, 'enemy') 
                
                for v in view:
                    if v.name == 'player':
                        cv2.rectangle(ROI, v.topLeft, v.bottomRight, color=(255,0,0), thickness=1, lineType=cv2.LINE_4)
                    if v.name == 'enemy':
                        cv2.rectangle(ROI, v.topLeft, v.bottomRight, color=(0,0,255), thickness=1, lineType=cv2.LINE_4)
                    if v.name == 'spider':
                       cv2.rectangle(ROI, v.topLeft, v.bottomRight, color=(0,100,255), thickness=1, lineType=cv2.LINE_4) 
                cv2.imshow('Computer Vision', ROI)
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
