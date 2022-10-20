from cgitb import text
from tkinter import Button
from turtle import title
import pyautogui as pg

pg.sleep(2)
# pg.alert(text="Alert", title='alert box', button='ok')
pg.confirm(text="Alert", title='alert box', buttons =['ok', 'cancel'])
print(pg.prompt(text="Enter the input: ", title="Input Box"))
print(pg.password(text="Enter the possword ", title="input box", mask="#" ))