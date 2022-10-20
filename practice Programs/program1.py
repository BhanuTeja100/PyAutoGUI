import pyautogui as pg

# prints the position of the cursor on the screen
pos = pg.position()
print(pos)

# prints the size of the screen
siz = pg.size()
print(siz)

# To find whether a point location is one the screen or not # Gives boolean value as output
pre = pg.onScreen(1910,10)
print(pre)
pre2 = pg.onScreen(2001, 2022)
print(pre2)

# Waits for 5 seconds using pause and move to will move the cursor to the index provided 
pg.PAUSE = 5
pg.moveTo(1724,127)
pg.PAUSE = 10
pg.moveTo(1088,1057)

