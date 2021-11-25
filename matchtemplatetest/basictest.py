import cv2, pyautogui, numpy as np 

game = cv2.imread('resources/MatchTemplateImages/screenshot 2.PNG', cv2.COLOR_BGR2GRAY)
imgCopy= game.copy()
en1 = cv2.imread('resources/MatchTemplateImages/enemy1.png', cv2.COLOR_BGR2GRAY)
en2 = cv2.imread('resources/MatchTemplateImages/enemy2.png', cv2.COLOR_BGR2GRAY)
spider = cv2.imread('resources/MatchTemplateImages/spider.png', cv2.COLOR_BGR2GRAY)

result = cv2.matchTemplate(imgCopy, spider, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_index, max_index = cv2.minMaxLoc(result)


spider_w = spider.shape[1]
spider_h = spider.shape[0]

top_left = max_index
bottom_right = (top_left[0] + spider_w, top_left[1] + spider_h)
cv2.rectangle(imgCopy, top_left, bottom_right, color=(255,0,0), thickness=2, lineType=cv2.LINE_4)


cv2.imshow('Result', imgCopy)
cv2.waitKey()
