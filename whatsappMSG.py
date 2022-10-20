import pyautogui as pyGUI
import time

# Python program to send 100  Happy Birthday messages in whatsapp 
i=0
name = input("Enter the name of the person who is celebrating birthday : ")
time.sleep(5)

while i < 10:
    time.sleep(0.1)
    pyGUI.typewrite("Happy Birthday " +  name + " :)") # You can also put name after happy Birthday
    pyGUI.press("enter")
    i = i+1

# Instructions  
""" 1.  Run the code 
    2. Enter the name of the person to whom you want to send wishes
    3. Switch to the other window where whatsapp is opened
    4. Put the cursor in the text box of the persons contact 
    5. Then the program automatically sends 100 messages one after the other """ 

