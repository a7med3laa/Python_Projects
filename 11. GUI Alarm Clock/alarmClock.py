# importing the required modules  
from tkinter import *  
import datetime as dt  
import time  
import winsound as ws  

# defining the function for the alarm clock  
def alarm():  
    while True:  
        time.sleep(1)  
        actualTime = dt.datetime.now()  
        currentTime = actualTime.strftime("%H : %M : %S") 
        currentDate = actualTime.strftime("%d / %m / %Y")  
        the_message = "Current Time: " + str(currentTime)  
        print(the_message) 
        if currentTime == alarmSetTime:  
            ws.PlaySound("sound.wav", ws.SND_ASYNC)  
            break  

# defining the function to set alarm clock 
# and check if time is valid or not
def getAlarmTime():  
    s='00'
    actualTime = dt.datetime.now()  
    h = actualTime.strftime("%H")
    m = actualTime.strftime("%M")  
    hr=int(hour.get())
    h=int(h)
    if  hr<h:
        timeFormat.config(text='wrong time')
    elif hr==h and int(minute.get())<int(m):
        timeFormat.config(text='wrong time')  
    else:
        global alarmSetTime 
        # variable alarmSetTime is global so any function can access
        alarmSetTime = f"{hour.get()} : {minute.get()} : {s}" 
        timeFormat.config(text="Next Alarm in "+str(alarmSetTime)+" press Start")
        print("Next Alarm in "+str(alarmSetTime))
        

# defining the function to stop alarm clock 
# and reset
def stopAlarm():
    ws.PlaySound(None,0)
    hourTime.delete(0,END)
    minuteTime.delete(0,END)
    timeFormat.config(text='')
  
# creating the GUI for the application  
guiWindow = Tk()  
guiWindow.title("The Alarm Clock")  
guiWindow.geometry("464x270")  
guiWindow.config(bg = "#87BDD8")  
guiWindow.resizable(width = False, height = False)  

timeFormat = Label(  
    guiWindow,  
    text = "Remember to set time in 24-hour format!",  
    font = ("Arial", 13)  
    )
timeFormat.place( x = 30,  y = 240 )  
   
add_time = Label(  
    guiWindow,  
    text = "Hour      Minute",  
    font = 60,  
    fg = "white",  
    bg = "#87BDD8"  
    ).place( x = 220, y = 10 )  
  
setAlarm = Label(  
    guiWindow,  
    text = "Set Time for Alarm: ",  
    fg = "white",  
    bg = "#034F84",  
    relief = "solid",  
    font = ("Helevetica", 13, "bold")  
    ).place(  x = 30, y = 50)  
   
hour = StringVar()  
minute = StringVar()  
   
hourTime = Entry(  
    guiWindow,  
    textvariable = hour,  
    bg = "#FEFBD8",  
    width = 4,  
    font = (20)  
    )

hourTime.place( x = 220,  y = 53 )  

minuteTime = Entry(  
    guiWindow,  
    textvariable = minute,  
    bg = "#FEFBD8",  
    width = 4,  
    font = (20)  
    )

minuteTime.place(  x = 297, y = 53  )  
   
submit = Button(  
    guiWindow,  
    text = "Set The Alarm",  
    fg = "white",  
    bg = "#82B74B",  
    width = 15,  
    command = getAlarmTime,  
    font = (20)  
    ).place(  x = 140,  y = 100 )  

start = Button(  
    guiWindow,  
    text = "Start",  
    fg = "white",  
    bg = "#82B74B",  
    width = 15,  
    command = alarm,  
    font = (20)  
    ).place(  x = 140,  y = 150 )  

   
stop = Button(  
    guiWindow,  
    text = "Stop",  
    fg = "white",  
    bg = "red",  
    width = 15,  
    command = stopAlarm,  
    font = (20)  
    ).place(  x = 140,  y = 200 )  

guiWindow.mainloop()  