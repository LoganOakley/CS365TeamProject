# after (what i did) installing OpenCV with cmd (pip install opencv-python)  or through opencv's github page (https://github.com/opencv/opencv/releases)
from cv2 import cv2 as cv
import numpy as np
# pyautogui needs a pip install, provides keyboard and mouse automation (use in our ai agent?)
import pyautogui
import os
import threading
# configparser is in case we want to implement ini files later
import configparser


# This is all sample OpenCV code
path = r'pacman_atarigame.png'

# Reading an image in default mode
image = cv.imread(path)


# Window name in which image is displayed
window_name = 'image'
hsv_win_name = 'hsv image'

hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)

# mask of green (36,0,0) ~ (70, 255,255)
mask1 = cv.inRange(hsv, (36, 0, 0), (70, 255, 255))

# mask o yellow (15,0,0) ~ (36, 255, 255)
mask2 = cv.inRange(hsv, (15, 0, 0), (36, 255, 255))


pacman = cv.inRange(hsv, (17, 0, 0), (17, 255, 255))
ghostsAndDots = cv.inRange(hsv, (43, 0, 0), (43, 255, 255))
score = cv.inRange(hsv, (64, 0, 0), (64, 255, 255))

# final mask and masked
mask = cv.bitwise_or(mask1, mask2)
target = cv.bitwise_and(hsv, hsv, mask=mask)

#target_pacman = cv.bitwise_and(hsv,hsv, mask=pacman)
#target_ghost = cv.bitwise_and(hsv,hsv, mask=ghostsAndDots)
#target_score = cv.bitwise_and(hsv,hsv, mask=score)
# Using cv2.imshow() method
# Displaying the image
cv.imshow(window_name, image)
cv.imshow('Masked Image HSV', target)
#cv.imshow('Pac-Man Location', target_pacman)
#cv.imshow('Ghost location', target_ghost)
#cv.imshow('Score', target_score)
# waits for user to press any key
# (this is necessary to avoid Python kernel form crashing)
cv.waitKey(0)

# closing all open windows
cv.destroyAllWindows()
