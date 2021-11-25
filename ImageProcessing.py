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

#testing if we can return an array of images
def regularGrayscale(img):
        processed_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(processed_img, 10, 100)
        contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
                cv2.drawContours(processed_img, [cnt], -1, (255, 255, 0), 1)
        return processed_img

def subtraction(img):
        subtract = cv2.createBackgroundSubtractorMOG2()
        processed_img = subtract.apply(img)
        edges = cv2.Canny(processed_img, 10, 100)
        contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
                # BGR for contour color
                cv2.drawContours(processed_img, [cnt], -1, (255, 0, 0), 1)
        return processed_img

def noFilter(img):
        img = np.ascontiguousarray(img)
        #edges = cv2.Canny(img, 10, 200)
        #contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        #for cnt in contours:
         #       area = cv2.contourArea(cnt)
          #      
           #     if area < 200:
            #            cv2.drawContours(img, [cnt], -1, (255, 0, 255), 1)
        return img