import time
import calendar
from tkinter import *
from tkinter import ttk
from tkinter import font
import winsound

h = 0
m = 0
s = 0
t = "am"

def current_time(h,m,s,t):

    
    totalSeconds = calendar.timegm(time.gmtime())
    currentSecond = totalSeconds%60
    

    totalMinutes= totalSeconds//60
    currentMinute= totalMinutes%60
    

    totalHours= totalMinutes//60
    currentHour= (totalHours%24)-6
    
    
    am_pm = ""
    if currentHour>= 12:
        am_pm="PM"
    if currentHour==0:
        currentHour=currentHour+12
    else:
        am_pm = "AM"
        if currentHour==0:
            currentHour=currentHour+12
    a= str(h)+":"+str(m)+":"+str(s)+t

    timex= str(currentHour)+":"+str(currentMinute)+":"+str(currentSecond) +" "+ am_pm
    if timex == a:
        beep()
    return timex

def beep():
    winsound.Beep(640.500)

def quit(*args):
    root.destroy()
    
def show_time():
    global h
    global m
    global s
    global t
    time = current_time(h,m,s,t)
    txt.set(time)
    root.after(1000, show_time)

def get_alarm(*args):
    global h
    h=input("what hour")
    global m
    m=input ("what minute")
    global s
    s=input("what second")
    global t
    t=input("am or pm").upper()


root = Tk()
# set window size
root.geometry("500x200")
root.attributes("-fullscreen",False)
# set window background color
root.configure(background='purple4')
# set up keys to do alarm or quit
root.bind("x", quit)
root.bind("a", get_alarm)
root.after(1000, show_time)
# set up font
fnt = font.Font(family='Commic Sans', size=60, weight='bold')
txt = StringVar()
# display time and set up the colors of text and background
lbl=ttk.Label(root, textvariable=txt, font=fnt, foreground="medium Blue", background='Red3')
# place the time in the center of screen
lbl.place(relx=0.5, rely=0.5, anchor= CENTER)

# start main loop
root.mainloop()
