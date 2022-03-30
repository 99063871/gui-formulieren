import tkinter
from tkinter.messagebox import askyesno
import random
import time
from turtle import pos

window = tkinter.Tk()
window.geometry("440x300")
window.configure(bg="gray")
window.title("Simple FPS trainer")
labelTime = tkinter.Label()
labelTime.config(bg="gray")
labelTime.pack()

labelPoints = tkinter.Label()
labelPoints.config(bg="gray")
labelPoints.pack()

list = ["Press: W", "Press: A", "Press: S","Press: D", "Press: Spacebar", "Single click", "Double click", "Triple click"]
score = 0
counter = 0
scoreCount = 0
timerSecs = 0
timeLeft=20
totalTime = 20

def submit():
    global timeLeft, totalTime
    if score == -1:
        timerSecs_var=timerSecs_entry.get()
        print("The name is : " + timerSecs_var)
        timerSecs_entry.destroy()
        if timerSecs_var != "":
            timeLeft = int(timerSecs_var)
            totalTime = timerSecs_var
        else:
            timeLeft == 20

def timer():
    global timerSecs, timeLeft, totalTime
    timerSecs+=1
    timeLeft-=1
    labelTime.config(text="Time remaining: "+str(timeLeft))
    if timerSecs == int(totalTime):
        button.destroy()
        answer = askyesno(title='Confirmation', message='Congratulations you have '+str(scoreCount)+' points, wanna play again?')
        if answer == True:
            restartFunc()
        else:
            window.destroy()
    else:
        labelTime.after(1000, timer)

def restartFunc():
    global timerSecs, scoreCount, commandVar, score, button, buttonVar, timeLeft, timerSecs_var, timerSecs_entry
    timerSecs=0
    score = 0
    timeLeft=20
    scoreCount=0
    timerSecs_var = 20
    timerSecs_entry = tkinter.Entry(window, textvariable = timerSecs_var, font = ('calibre',10,'normal'))
    timerSecs_entry.pack()
    commandVar = random.choice(list)
    button = tkinter.Button(text="Click here to start", bg="White", borderwidth=0, height=2)
    button.place(x=180, y=120)
    buttonVar = '<Button-1>'
    button.bind(buttonVar , fpsFunction)
    score-=1

def fpsFunction(e):
    global scoreCount, commandVar, buttonVar, score, events
    submit()
    events = "nope"
    score+=1
    window.unbind(buttonVar)
    button.unbind(buttonVar)
    commandVar = random.choice(list)
    button.config(text=commandVar)
    button.place(x=random.randint(0,360), y=random.randint(0, 250))
    
    if commandVar == "Press: W":
        buttonVar = '<w>'
    elif commandVar == "Press: A":
        buttonVar = '<a>'
    elif commandVar == "Press: S":
        buttonVar = '<s>'
    elif commandVar == "Press: D":
        buttonVar = '<d>'
    elif commandVar == "Press: Spacebar":
        buttonVar = '<space>'
    elif commandVar == "Single click":
        buttonVar = '<Button-1>'
        events = "click"
    elif commandVar == "Double click":
        buttonVar = '<Double-Button-1>'
        events = "click"
    elif commandVar == "Triple click":
        buttonVar = '<Triple-Button-1>'
        events = "click"
    if events == "click":
        button.bind(buttonVar, fpsFunction)
        scoreCount+=2
    else:
        window.bind(buttonVar, fpsFunction)
        scoreCount+=1
    labelPoints.config(text=str(scoreCount)+" points")
    if timerSecs == 0:
        timer()

timerSecs_var = 20
timerSecs_entry = tkinter.Entry(window, textvariable = timerSecs_var, font = ('calibre',10,'normal'))
timerSecs_entry.pack()

commandVar = random.choice(list)
button = tkinter.Button(text="Click here to start", bg="White", borderwidth=0, height=2)
button.place(x=180, y=120)
buttonVar = '<Button-1>'
button.bind(buttonVar , fpsFunction)
score-=1

window.mainloop()