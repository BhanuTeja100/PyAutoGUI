from cgitb import text
from turtle import title
import pyautogui as pg

test = pg.confirm(text = "Do you want login? ", title="Login", buttons= ['Yes', 'No'])

if test == 'Yes':
    username = pg.prompt(text="Enter the Username: ", title="Username")
    password = pg.password(text="Enter the Password", title="Password",mask='$' )

elif test == 'No':
   con =  pg.confirm(text = "Are You Sure ? ", title="Alert", buttons= ['Yes', 'No'])
   if con == 'Yes':
    print("User Don't want to Login")
    quit()

   elif con == 'No':
    print("Please Try Again")

print(f"Username is: {username} \nPassword is: {password}")