import pyautogui as pyGUI
import time
i=0
time.sleep(2)
pyGUI.typewrite("Bro my program is running i can send hundred messages in a minute ")
    
while i < 100:
    time.sleep(0.1)
    pyGUI.typewrite("Hi Prends\n")
    pyGUI.typewrite("Bye Prends\n")
    pyGUI.press("enter")
    i = i+1

