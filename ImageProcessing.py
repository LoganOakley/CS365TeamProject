from cv2 import cv2 as cv2
import numpy as np
def detectEdges(img):

        processed_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        processed_img = cv2.Canny(processed_img, threshold1=50, threshold2=100)
        processed_img = np.ascontiguousarray(processed_img)
        return processed_img
    
