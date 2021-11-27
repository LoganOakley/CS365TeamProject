import cv2, pyautogui, numpy as np, os


def drawBoxes(image,template):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_index, max_index = cv2.minMaxLoc(result)

    threshold = .6
    if max_val >= threshold:


        template_w = template.shape[1]
        template_h = template.shape[0]

        top_left = max_index
        bottom_right = (top_left[0] + template_w, top_left[1] + template_h)
        cv2.rectangle(image, top_left, bottom_right, color=(255,0,0), thickness=2, lineType=cv2.LINE_4)
    return image




