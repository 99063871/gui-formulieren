from msilib.schema import AdminExecuteSequence, CheckBox
import tkinter
from tkinter import *
import threading

lastbutton = 0
amount = 0

def commandPressUp(e):
    global lastbutton
    global amount
    lastbutton = "up"
    amount+=1
    label.configure(text=round(amount, 1))
    numberCheck()

def commandPressDown(e):
    global lastbutton
    global amount
    lastbutton = "down"
    amount-=1
    label.configure(text=round(amount, 1))
    numberCheck()

def commandUp():
    global lastbutton
    global amount
    checkBox.config(state=NORMAL)
    lastbutton = "up"
    amount+=1
    label.configure(text=round(amount, 1))
    numberCheck()

def commandDown():
    global lastbutton
    global amount
    checkBox.config(state=NORMAL)
    lastbutton = "down"
    amount-=1
    label.configure(text=round(amount, 1))
    numberCheck()

window = tkinter.Tk()
window.geometry("300x250")
def numberCheck():
    if amount == 0:
        window.configure(bg="gray")
    elif amount >=1:
        window.configure(bg="green")
    elif amount <=1:
        window.configure(bg="red")

def labelHover(e):
    window.configure(bg="yellow")

def labelLeave(e):
    numberCheck()

def doubleClick(e):
    global amount
    if lastbutton == "up":
        amount*=3
    elif lastbutton == "down":
        amount/=3
    label.configure(text=round(amount, 1))
    label.config()
    numberCheck()
 
def commands():
    commandUp()

def checkBoxFunc():
    if checkboxState.get()==1:
        if lastbutton == "up":
            commandUp()
            threading.Timer(0.5, checkBoxFunc).start()
        else:
            commandDown()
            threading.Timer(0.5, checkBoxFunc).start()
        

checkboxState=tkinter.IntVar(value=1)
checkBox = tkinter.Checkbutton(window, variable=checkboxState, state=DISABLED, command=checkBoxFunc)
checkBox.pack()

numberCheck()
buttonUp = tkinter.Button(text= "Up", command=commandUp, width=50, background="white", padx=100)
buttonUp.pack(

            fill='both',

            expand=True,

            pady=20,

            padx=20

        )

label = tkinter.Label(text=amount, width=50, background="white")
label.bind("<Enter>", labelHover)
label.bind("<Leave>", labelLeave)
label.pack(

            fill='both',

            expand=True,

            pady=20,

            padx=20

        )

buttonDown = tkinter.Button(window, text= "Down", command=commandDown, width=50, background="white")
buttonDown.pack(

            fill='both',

            expand=True,

            pady=20,

            padx=20

        )

label.bind('<Double-Button-1>', doubleClick)
window.bind('<space>', doubleClick)
window.bind('<Up>', commandPressUp)
window.bind('+', commandPressUp)
window.bind('-', commandPressDown)
window.bind('<Down>', commandPressDown)
window.mainloop()