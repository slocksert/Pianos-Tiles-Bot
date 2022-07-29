import cv2
import numpy as np
import pyautogui
from mss import mss
import time

start_y = 540
start_x = 595

box = (start_x, start_y, start_x+375, start_y+1)

cords_x = [0, 125, 250, 374]

def click(x,y):
    pyautogui.click(x,y)

def start():
    while True:
        with mss() as sct:
            img = sct.grab(box)
            for cord in cords_x:
                if img.pixel(cord, 0)[0] < 100:
                    click(start_x+cord, start_y)
                    break


time.sleep(5)
start()


""" pic = pyautogui.screenshot(region=(400,150,550,300))
pic.save('teste.png')
game_img = cv2.imread('teste.png', cv2.IMREAD_COLOR)
game_img = game_img.astype(np.float32)
box_img = cv2.imread('box.png', cv2.IMREAD_COLOR)
box_img = box_img.astype(np.float32)

result = cv2.matchTemplate(game_img, box_img, cv2.TM_CCORR_NORMED)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

def click(x,y):
    pyautogui.click(x,y)

click(max_loc[0],max_loc[1])
 """
