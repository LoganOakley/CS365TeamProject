import numpy as np
from PIL import ImageGrab
import cv2


def process_img(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img,threshold1=50, threshold2=100)
    return processed_img

while(True):
    screen =  np.array(ImageGrab.grab(bbox=(0,40,800,640)))
    new_screen = process_img(screen)
    #printscreen_numpy = cv2.cvtColor(screen,cv2.COLOR_BGR2RGB)
    cv2.imshow('window',new_screen)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break