import cv2, pyautogui, numpy as np, os

class GameObjects:
    
    topLeft = []
    bottomRight = []
    pastx = 0 #not implemented yet
    pasty = 0 #not implemented yet
    name = ''
    
    def __init__(self, topleftlocation, botRightlocation, name):
        self.topLeft = topleftlocation
        self.bottomRight = botRightlocation
        self.name = name
    
    

def drawBoxes(image,template,name = ''):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    w, h = template.shape[::-1]
    #min_val, max_val, min_index, max_index = cv2.minMaxLoc(result)
    gameObjects = []
    

    threshold = .6
    loc = np.where(result >= threshold)
    for p in zip(*loc[::-1]):
        gameObjects.append(GameObjects(p, (p[0] + w, p[1] + h), name))
    #if max_val >= threshold:
#
#
 #       template_w = template.shape[1]
  #      template_h = template.shape[0]
#
 #       top_left = max_index
  #      bottom_right = (top_left[0] + template_w, top_left[1] + template_h)
   #     #cv2.rectangle(image, top_left, bottom_right, color=(255,0,0), thickness=2, lineType=cv2.LINE_4)
    #    gameObjects.append(GameObjects(top_left, bottom_right, name))
    return gameObjects




