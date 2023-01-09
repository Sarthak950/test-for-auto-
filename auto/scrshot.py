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

# gameCoords = [657, 32, 1262, 1039]
# gameCoords = [100, 100, 1920, 1080]
# gameCoords = [711, 1324, 1079, 1919]
# gameCoords = [1314, 319, 1362, 752]
gameCoords = [850, 204, 894, 248]
increment = 2

# take a screen shot of the cordinates and read the pixelvalue at the cordinate 10, 10 


def screenGrab():
    box = (gameCoords[0],gameCoords[1],gameCoords[2],gameCoords[3])
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    return im


def processImg(original_image):
    processed_img = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
    processed_img = cv2.Canny(processed_img, threshold1 = 200, threshold2=300)
    return processed_img

def exit():
    print('exit')
    cv2.destroyAllWindows()
    quit()


def paste(data,i):
    pyautogui.click(1347, 65, duration=0.2) # hamburger menu

    print(i+1)

    if i%3 == 1:
        pyautogui.click(1353,229,duration=1) # first id
    elif i%3 == 2:
        pyautogui.click(1353,279,duration=1) # second id
    else:
        pyautogui.click(1353,329,duration=1) # third id 

    pyautogui.click(1353, 136, duration=0.2) # chat
    # pyautogui.click(1353, 206, duration=0.2) 
    # pyautogui.click(1353, 289, duration=0.2) 

    pyautogui.click(1402, 995, duration=0.2) # typing box
    pyautogui.typewrite(data)

    pyautogui.click(1353, 57, duration=0.2) # <-

def pastecopy(data,i):
    pyautogui.click(1429, 938, duration=0.2) # typing box
    pyautogui.typewrite(data)
    pyautogui.press('enter')


def do_job(i):
    # break if user move mouse
    # if pyautogui.position() != (0,0):
    #     print('user moved mouse')
    #     return
    # right click on 850 ,204 duraion = 0.1
    pyautogui.click(850 + 22, 204 + 22, button='right', duration=0.1)
    pyautogui.click(906,296, button='left', duration=0.2)
    # time.sleep(2)
    pyautogui.click(1408,789 ,duration=0.2)

    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()

    # paste(data,i);
    pastecopy(data,i);
    pyautogui.click(868, 170, duration=0.5) #clicking on empty space

    pyautogui.scroll(-40)



def main():
    last_time = time.time()
    
    i=0
    while(True):

        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
        screen =  np.array(screenGrab())

        curr_time = time.time()
        

        new_screen = processImg(screen)
        cv2.imshow('window', new_screen)
        
        # add scroll  
        pyautogui.scroll(-5)



        # iterate over the np array 
        for j in range(0, len(new_screen),increment):
            # for j in range(0, len(new_screen[i]),increment):
                if new_screen[5][j] > 100:
                    print('hurray')
                    do_job(i)
                    i+=1
                    break

        # delete the taken screenshot
        os.remove(os.getcwd() + '\\full_snap__' + str(int(curr_time)) + '.png')
        
main()

