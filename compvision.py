# after (what i did) installing OpenCV with cmd (pip install opencv-python)  or through opencv's github page (https://github.com/opencv/opencv/releases)
from cv2 import cv2 as cv
import numpy as np
# pyautogui needs a pip install, provides keyboard and mouse automation (use in our ai agent?)
import pyautogui
import os


# This is all sample OpenCV code
path = r'Computer Vision.png'

# Reading an image in default mode
image = cv.imread(path)

# Window name in which image is displayed
window_name = 'image'

# Using cv2.imshow() method
# Displaying the image
cv.imshow(window_name, image)

# waits for user to press any key
# (this is necessary to avoid Python kernel form crashing)
cv.waitKey(0)

# closing all open windows
cv.destroyAllWindows()
