import pyautogui
import time
f = open("data_set/day_7.txt",encoding="utf8")

for i in range(12):
    pyautogui.click(1199, 126,duration=0.7) # locatin of the chat
    pyautogui.click(1442,993,duration=0.7) # typing bar
    # pyautogui.typewrite(f.readline())  
    pyautogui.click(996,66,duration=1) #id change bar
        
    if i%3 == 1:
        pyautogui.click(1001,231,duration=1) # first id
    elif i%3 == 2:
        pyautogui.click(1001,283,duration=1) # second id
    else:
        pyautogui.click(1001,340,duration=1) # third id  
    print(i+1)
time.sleep(1000);
# 4