import numpy as np
# import PIL 
from PIL import ImageGrab,Image
import cv2
import ctypes
import pyautogui
import time
import os
import paperclip
import win32clipboard

gameCoords = [872, 277, 916, 321]

def screenGrab():
    box = (gameCoords[0],gameCoords[1],gameCoords[2],gameCoords[3])
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return im


def processImg(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1 = 200, threshold2=300)
    return processed_img


while True:
        screen =  np.array(screenGrab())

        curr_time = time.time()
        

        new_screen = processImg(screen)
        cv2.imshow('window', new_screen)
