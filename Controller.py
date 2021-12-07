from configparser import Error

from win32con import LC_INTERIORS
from DirectKeyInputs import ReleaseKey, PressKey, LEFT, RIGHT, UP, DOWN, SPACE, F2
import time
import win32gui
import math
from threading import Thread
from Tracking import GameObjects

def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
def bringToFront():
    
    results = []
    top_windows = []
    win32gui.EnumWindows(windowEnumerationHandler, top_windows)

    for i in top_windows:
        if "stella" in i[1].lower():
            print(i)
            win32gui.ShowWindow(i[0],5)
            win32gui.SetForegroundWindow(i[0])
            break

def Start():
    PressKey(F2)
    time.sleep(.1)
    ReleaseKey(F2)
def GoUp():
    PressKey(UP)
    ReleaseKey(DOWN)
    #ReleaseKey(LEFT)
    #ReleaseKey(RIGHT)

def GoDown():
    PressKey(DOWN)
    ReleaseKey(UP)
    #ReleaseKey(LEFT)
    #ReleaseKey(RIGHT)
    
def GoLeft():
    PressKey(LEFT)
    #ReleaseKey(DOWN)
    #ReleaseKey(UP)
    ReleaseKey(RIGHT)
    
def GoRight():
    PressKey(RIGHT)
    #ReleaseKey(DOWN)
    #ReleaseKey(UP)
    ReleaseKey(LEFT)    

def Stop():
    ReleaseKey(RIGHT)
    ReleaseKey(DOWN)
    ReleaseKey(UP)
    ReleaseKey(LEFT)
def Shoot():
    PressKey(SPACE)
    time.sleep(.01)
    ReleaseKey(SPACE)
    
    
def DetermineActions(player, enemyLocations, spiderObject = None):
    down = False
    up = False
    right = False
    left = False
    stop = False
    shoot = False
    enemyAbove = False
    enemyBelow = False
    closestEnemyDistance = 999.99
    closestEnemyX = 0
    emergencyDodge = False
    #if (spiderObject != None and spiderObject.position == 'above'):
        #print("spider above")
    for l in enemyLocations:
        
        
        if(l.name == "enemy" or l.name == "spider"):  
            enemyDistance = distance(l.topLeft, player)
            
            if(l.position == 'above'):
                if (l.bottomRight[1] + 20 > player[1] and (l.bottomRight[0] - 40 < player[0] and l.bottomRight[0] + 40 > player[0])):
                    enemyAbove = True
                if (l.topLeft[0] > player[0]): #shoot logic
                
                    if (l.topLeft[0] - player[0] < 20):
                        Shoot()
                    
                else:
                    if (player[0] - l.topLeft[0] < 20):
                        Shoot()
            else:
                if ((l.bottomRight[1] - 20 < player[1] and l.bottomRight[1] + 20 > player[1])and (l.bottomRight[0] - 40 < player[0] and l.bottomRight[0] + 40 > player[0])):
                    enemyBelow = True
                
            #if(l.topleft[0] - 30 < player[0] and l.topLeft + 30 > player[0]):
            if (enemyDistance < closestEnemyDistance):
                #print(f'{enemyDistance}')
                closestEnemyDistance = enemyDistance
                closestEnemyX = l.bottomRight[0] - 10
                #print(f"new enemy distance: {closestEnemyDistance}")
                if ((l.bottomRight[1] > player[1] - 20 and l.bottomRight[1] < player[1] + 20)):
                    if (enemyDistance < 15):
                        print("emergency dodge activated!")
                        emergencyDodge = True
                    #print("made it to actions")
                    if(l.bottomRight[0] < player[0]):
                        right = True
                        left = False
                        #GoRight()
                    else:
                        left = True
                        right = False
                        #GoLeft()
                    if(enemyAbove == False and player[1] > 485):
                        up = True
                        down = False
                        #GoUp()
                    elif(enemyBelow == False and player[1] < 555):
                        down = True
                        up = False
                        #GoDown()
                elif ((player[0] < closestEnemyX + 20 and player[0] > closestEnemyX - 20)):
                    print("stopped")
                    stop = True
                elif (spiderObject != None):
                    if (player[0] < closestEnemyX): #or (player[0] > spiderObject.bottomRight[0] and player[0] - spiderObject.bottomRight[0] < 20 and spiderObject.position == 'below')):
                        print("chasing right")
                        right = True
                        left = False
                    elif (player[0] > closestEnemyX): # or (player[0] < spiderObject.bottomRight[0] and spiderObject.bottomRight[0] - player[0] < 20 and spiderObject.position == 'below')):
                        print("chasing left")
                        left = True
                        right = False
                elif (player[1] < 485 and (closestEnemyX + 30 < player[0] or closestEnemyX - 30 > player[0])):
                    print("did downward dodge")
                    down = True
                    up = False
                else:
                    stop = True
                    
            #if (((l.topLeft[0] + l.bottomRight[0]) / 2) - 30 > player[0] or  ((l.topLeft[1] + l.bottomRight[1]) / 2) + 30 < player[0]):    if you want to use center of object
            
            
            
            
            
                
            
        
        
    
    if (shoot == True):
        Shoot()
    if (emergencyDodge == True):
        if (player[1] < 485):
            if (closestEnemyX > player[0]):
                GoLeft()
            else:
                GoRight()
            GoDown()
        elif(player[1] > 555):
            if (closestEnemyX > player[0]):
                GoLeft()
            else:
                GoRight()
            GoUp()
        else:
            if (closestEnemyX > player[0]):
                GoLeft()
            else:
                GoRight()
    else: 
        if (stop):
            Stop()
        else:
            if (up):
                GoUp()
            elif(down):
                GoDown()
            
            if (right):
                GoRight()
            elif (left):
                GoLeft()


            
            
    
        
    
        

def distance(loc1,loc2):
    return math.sqrt((loc1[1]-loc1[0])**2+(loc2[1]-loc2[0])**2)

    


