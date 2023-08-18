from tkinter import *

master = Tk()

# set the title of GUI window
master.title("Distance Converter")


def convert():
    #get the current value to be converted
    current=int(e.get())
    #options of distance
    options=["Kilometer (Km)",
            "meter (m)", "foot","yard","mile"]
    #Get two options from dropdown list
    d_from=variable.get()
    d_to=variable2.get()

    #convert value from one distance to another
    #from meter to all
    #from meter to KM
    if(d_from==options[1] and d_to==options[0]):
        res=current*1000
        lb_val.config(text = str(res)+"Km")
    #from meter to meter do nothing
    elif(d_from==options[1] and d_to==options[1]):
        res=current
        lb_val.config(text = str(res)+"m")
    #from meter to foot
    elif(d_from==options[1] and d_to==options[2]):
        res=current*3.281
        lb_val.config(text = str(res)+"ft")
    #from meter to yard
    elif(d_from==options[1] and d_to==options[3]):
        res=current*1.094
        lb_val.config(text = str(res)+"yd")
    #from meter to mile
    elif(d_from==options[1] and d_to==options[4]):
        res=current/1609
        lb_val.config(text = str(res)+"mi")

    #from Km to all
    #from Km to KM
    if(d_from==options[0] and d_to==options[0]):
        res=current
        lb_val.config(text = str(res)+"km")
    elif(d_from==options[0] and d_to==options[1]):
        res=current*1000
        lb_val.config(text = str(res)+"m")
    elif(d_from==options[0] and d_to==options[2]):
        res=current*3281
        lb_val.config(text = str(res)+"ft")
    elif(d_from==options[0] and d_to==options[3]):
        res=current*1094
        lb_val.config(text = str(res)+"yd")
    elif(d_from==options[0] and d_to==options[4]):
        res=current/1.609
        lb_val.config(text = str(res)+"mi")

#define clear function
def button_clear():
    lb_val.config(text ="")
    e.delete(0,END)

lb_from=Label(master,text="Form: ")
lb_to=Label(master,text="To: ")
lb_from.grid(row=0,column=0,padx=10,pady=10)
lb_to.grid(row=1,column=0,padx=10,pady=10)
lb_msg=Label(master,text="Value to Convert")
lb_msg.grid(row=2,column=0,columnspan=2,padx=10,pady=10)
lb_res=Label(master,text="Result : ")
lb_res.grid(row=5,column=0,padx=10,pady=10)
lb_val=Label(master,text="")
lb_val.grid(row=5,column=1,padx=10,pady=10)


e=Entry(master,width=30,borderwidth=5)
e.grid(row=3,column=0,columnspan=2,padx=20,pady=20)

variable = StringVar(master)
variable.set("meter (m)") # default value

dist_from= OptionMenu(master, variable,"Kilometer (Km)"
 , "meter (m)")
dist_from.grid(row=0,column=1,padx=20,pady=20)

variable2 = StringVar(master)
variable2.set("foot") # default value

dist_to=OptionMenu(master, variable2,"Kilometer (Km)"
 , "meter (m)", "foot","yard","mile")
dist_to.grid(row=1,column=1,padx=20,pady=20)

btn_calc=Button(master,text="Convert",padx=30,pady=20,command=convert)
btn_calc.grid(row=4,column=0,padx=20,pady=10)
btn_clear=Button(master,text="Clear",padx=30,pady=20,command=button_clear)
btn_clear.grid(row=4,column=1,padx=20,pady=10)

mainloop()