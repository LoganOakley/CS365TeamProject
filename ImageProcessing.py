from cv2 import cv2 as cv2
import numpy as np
def detectEdges(img):

        processed_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        processed_img = cv2.Canny(processed_img, threshold1=50, threshold2=100)
        processed_img = np.ascontiguousarray(processed_img)
        return processed_img

def filterPurple(img):
        processed_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        purple_lower_bound = np.array([300,0,0])
        purple_upper_bound = np.array([360,255,255])
        processed_img = cv2.inRange(processed_img,purple_lower_bound,purple_upper_bound)
        return processed_img

def regularGrayscale(img):
        processed_img = [cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), cv2.cvtColor(img, cv2.COLOR_BGR2RGB)]
        return processed_img[0]