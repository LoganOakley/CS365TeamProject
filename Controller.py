from configparser import Error

from win32con import LC_INTERIORS
from DirectKeyInputs import ReleaseKey, PressKey, LEFT, RIGHT, UP, DOWN, SPACE, F2
import time
import win32gui

def windowEnumerationHandler(hwnd, top_windows):
    top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))

if __name__ == "__main__":
    results = []
    top_windows = []
    win32gui.EnumWindows(windowEnumerationHandler, top_windows)

    for i in top_windows:
        if "stella" in i[1].lower():
            print(i)
            win32gui.ShowWindow(i[0],5)
            win32gui.SetForegroundWindow(i[0])
            break
        

    


def quickTap(keyName):
    PressKey(keyName)
    time.sleep(.1)
    ReleaseKey(keyName)
    time.sleep(.1)

quickTap(F2)
print("up")
quickTap(UP)
print("down")
quickTap(DOWN)
print("left")
quickTap(LEFT)
print("right")
quickTap(RIGHT)
print('space')
quickTap(SPACE)