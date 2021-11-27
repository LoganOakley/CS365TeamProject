from configparser import Error

from win32con import LC_INTERIORS
from DirectKeyInputs import ReleaseKey, PressKey, LEFT, RIGHT, UP, DOWN, SPACE, F2
import time
import win32gui

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
    ReleaseKey(LEFT)
    ReleaseKey(RIGHT)

def GoDown():
    PressKey(DOWN)
    ReleaseKey(UP)
    ReleaseKey(LEFT)
    ReleaseKey(RIGHT)
    
def GoLeft():
    PressKey(LEFT)
    ReleaseKey(DOWN)
    ReleaseKey(UP)
    ReleaseKey(RIGHT)
    
def GoRight():
    PressKey(RIGHT)
    ReleaseKey(DOWN)
    ReleaseKey(UP)
    ReleaseKey(RIGHT)

def Shoot():
    PressKey(SPACE)
    time.sleep(.01)
    ReleaseKey(SPACE)
    


