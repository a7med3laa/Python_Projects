from tkinter import *
from tkinter import messagebox
import math



root= Tk()

# set the title of GUI window
root.title("Simple Calculator")

# set the configuration of GUI window
root.geometry("230x400")

# entry to get input and print output GUI window
e=Entry(root,width=30,borderwidth=5)
e.grid(row=0,column=0,columnspan=4,padx=20,pady=20)

#define button_click function
def button_click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

#define clear function
def button_clear():
    e.delete(0,END)

#define add function
def add():
    global operation
    global firstnumber
    operation="+"
    firstnumber=e.get()
    e.delete(0,END)

#define sub function
def sub():
    global operation
    global firstnumber
    operation="-"
    firstnumber=e.get()
    e.delete(0,END)

#define multi function
def multi():
    global operation
    global firstnumber
    operation="*"
    firstnumber=e.get()
    e.delete(0,END)

#define divid function
def divid():
    global operation
    global firstnumber
    operation="/"
    firstnumber=e.get()
    e.delete(0,END)

#define factorial function
def button_fact():
    global firstnumber
    firstnumber=e.get()
    total=1
    for num in range(1,int(firstnumber)+1):
        total=total*num
    e.delete(0,END)
    e.insert(0,total)

#define power function
def button_pow():
    global firstnumber
    firstnumber=e.get()
    total=pow(int(firstnumber),2)
    e.delete(0,END)
    e.insert(0,total)

#define suare root function
def button_root():
    global firstnumber
    firstnumber=e.get()
    total=math.sqrt(int(firstnumber))
    e.delete(0,END)
    e.insert(0,total)

#define equal function
def equal():
    secondnumber=e.get()
    total=0
    e.delete(0,END)
    if operation=="+":
        total=float(firstnumber)+float(secondnumber)
    elif operation=='-':
        total=float(firstnumber)-float(secondnumber)
    elif operation=='*':
        total=float(firstnumber)*float(secondnumber)
    elif operation=='/':
        try:
            total = float(firstnumber)/float(secondnumber)  
            # handles zerodivision exception
        except ZeroDivisionError:
            messagebox.showinfo("Error", "Can't divide by zero")

    e.insert(0,total)


#define buttons
button1=Button(root,text='1',padx=10,pady=10,command=lambda: button_click("1"))
button2=Button(root,text='2',padx=10,pady=10,command=lambda: button_click("2"))
button3=Button(root,text='3',padx=10,pady=10,command=lambda: button_click("3"))
button4=Button(root,text='4',padx=10,pady=10,command=lambda: button_click("4"))
button5=Button(root,text='5',padx=10,pady=10,command=lambda: button_click("5"))
button6=Button(root,text='6',padx=10,pady=10,command=lambda: button_click("6"))
button7=Button(root,text='7',padx=10,pady=10,command=lambda: button_click("7"))
button8=Button(root,text='8',padx=10,pady=10,command=lambda: button_click("8"))
button9=Button(root,text='9',padx=10,pady=10,command=lambda: button_click("9"))
button0=Button(root,text='0',padx=10,pady=10,command=lambda: button_click("0"))

button_sum=Button(root,text='+',padx=10,pady=10,command=add)
button_multi=Button(root,text='*',padx=10,pady=10,command=multi)
button_divid=Button(root,text='/',padx=10,pady=10,command=divid)
button_sub=Button(root,text='-',padx=10,pady=10,command=sub)
button_equal=Button(root,text='=',padx=10,pady=10,command=equal)
button_clear=Button(root,text='C',padx=10,pady=10,command=button_clear)
button_fact=Button(root,text='!',padx=10,pady=10,command=button_fact)
button_dot=Button(root,text='.',padx=10,pady=10,command=lambda: button_click("."))
button_pow=Button(root,text='^2',padx=10,pady=10,command=button_pow)
button_root=Button(root,text='√',padx=10,pady=10,command=button_root)

# put buttons on screen
# buttons in row 1
button_clear.grid(row=1,column=0,padx=10,pady=10)
button_fact.grid(row=1,column=1,padx=10,pady=10)
button_pow.grid(row=1,column=2,padx=10,pady=10)
button_root.grid(row=1,column=3,padx=10,pady=10)

# buttons in row 2
button7.grid(row=2,column=0,padx=10,pady=10)
button8.grid(row=2,column=1,padx=10,pady=10)
button9.grid(row=2,column=2,padx=10,pady=10)
button_divid.grid(row=2,column=3,padx=10,pady=10)

# buttons in row 3
button4.grid(row=3,column=0,padx=10,pady=10)
button5.grid(row=3,column=1,padx=10,pady=10)
button6.grid(row=3,column=2,padx=10,pady=10)
button_multi.grid(row=3,column=3,padx=10,pady=10)

# buttons in row 4
button1.grid(row=4,column=0,padx=10,pady=10)
button2.grid(row=4,column=1,padx=10,pady=10)
button3.grid(row=4,column=2,padx=10,pady=10)
button_sub.grid(row=4,column=3,padx=10,pady=10)

# buttons in row 5
button_sum.grid(row=5,column=3,padx=10,pady=10)
button0.grid(row=5,column=0,padx=10,pady=10)
button_dot.grid(row=5,column=1,padx=10,pady=10)
button_equal.grid(row=5,column=2,padx=10,pady=10)

# print GUI app
root.mainloop()