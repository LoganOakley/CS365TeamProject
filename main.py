from Controller import GoLeft, GoRight, Shoot, Start, Stop, bringToFront, DetermineActions, distance
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
            spider2 = cv2.imread('resources/MatchTemplateImages/spider.png')
            enMiddle = cv2.imread('resources/MatchTemplateImages/enemyMiddle.png')
            enEnd = cv2.imread('resources/MatchTemplateImages/enemyEnd.png')
            enEnd2 = cv2.imread('resources/MatchTemplateImages/enemyEnd2.png')
            player = cv2.imread('resources/MatchTemplateImages/PlayerSprite.png')
            playerloc = [600,600]
            spiderloc =[0,0]
            Start()
            while(True):
                #Stop()
                screenshot = wincap.grab_screenshot()
                ROI = screenshot[0:math.ceil(wincap.height * .85), math.ceil(wincap.width * .08):math.ceil(wincap.width*.92)]
                #ROI = screenshot[0:410,0:600] Quaid Note, this incorrectly sizes my stella window
                view = getLocations(ROI,player,'player',.8)
                view += getLocations(ROI, enMiddle, 'enemy', .8)
                #view += getLocations(ROI, enEnd, 'enemy', .9)
                #view += getLocations(ROI, enEnd2, 'enemy', .9)
                view += getLocations(ROI, spider, 'spider', .9)
                #view += getLocations(ROI, spider2, 'spider', .9)
                #view = view + drawBoxes(ROI, en2, 'enemy') 
                spiderobj = None
                enemyList = []
                for v in view:
                    if v.name == 'player':
                        playerloc = [(v.topLeft[0] + v.bottomRight[0]) / 2, v.topLeft[1]]
                        #print(f"{playerloc[0]}")
                        cv2.rectangle(ROI, v.topLeft, v.bottomRight, color=(0,0,255), thickness=1, lineType=cv2.LINE_4)
                    if v.name == 'enemy':
                        v.position = 'above' if v.bottomRight[1] < playerloc[1] else 'below'
                        enemyList.append(v)
                        cv2.rectangle(ROI, v.topLeft, v.bottomRight, color=(255,0,255), thickness=1, lineType=cv2.LINE_4)
                    if v.name == 'spider':
                        v.position = 'above' if v.bottomRight[1] < playerloc[1] else 'below'
                        enemyList.append(v)
                        cv2.rectangle(ROI, v.topLeft, v.bottomRight, color=(0,255,255), thickness=1, lineType=cv2.LINE_4)
                        spiderobj = v
                #print(" player:"+str(playerloc[0])+","+str(playerloc[1])+" spider:"+str(spiderloc[0])+","+str(spiderloc[0])+" Distance:"+str(distance(playerloc,spiderloc)))
                
                t1 = Thread(DetermineActions(playerloc, enemyList, spiderobj))
                t1.start()
                
                cv2.imshow('Computer Vision', ROI)
                count = myCounter.countPerSec()
                #print(count)
                myCounter.increment()
                
                #GoLeft()
                #Shoot()
                key = cv2.waitKey(1)
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


