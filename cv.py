#after (what i did) installing OpenCV with cmd (pip install opencv-python)  or through opencv's github page (https://github.com/opencv/opencv/releases)
import cv2 as cv


# This is all sample OpenCV code
path = r'Computer Vision.png'
  
# Reading an image in default mode
image = cv.imread(path)
  
# Window name in which image is displayed
window_name = 'image'
  
# Using cv2.imshow() method 
# Displaying the image 
cv2.imshow(window_name, image)
  
#waits for user to press any key 
#(this is necessary to avoid Python kernel form crashing)
cv2.waitKey(0) 
  
#closing all open windows 
cv2.destroyAllWindows() 