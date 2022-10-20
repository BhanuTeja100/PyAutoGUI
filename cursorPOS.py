# Program to print the cursor position constantly
import pyautogui as pg
import time

while True:
    x, y = pg.position()
    print(f"X:{x}, Y:{y} \n")
    pg.sleep(1)


# Instructions

""" 1. Run the program in the terminal 
2.Change the cursor position every second and you can the terminal printing different position values
"""