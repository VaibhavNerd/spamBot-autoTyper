
import pyautogui
import time
time.sleep(5)
f=open("spamText.txt",'r')
howManyTimes = 3 
for i in range (howManyTimes): 
    f.seek(0)
    for word in f:
      pyautogui.typewrite(word)           
      pyautogui.press("enter")
      time.sleep(0.5)
    
    











