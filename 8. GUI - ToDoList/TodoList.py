from tkinter import *
from tkinter import messagebox

global ToDoList
ToDoList=['Add new task']
global count
count=1

def addToList ():
    global count
    task=e.get()
    if ToDoList[0]=='Add new task':
        ToDoList.clear()
        lb.delete(0, END)
    
    
    if task != "":
        numbered_task=str(count)+'. '+task
        lb.insert(END, numbered_task)
        ToDoList.append(task)
        count+=1
        e.delete(0, END)
    else:
        messagebox.showwarning("warning", "Please enter some task.")


def deleteFromList():
     
    for i in lb.curselection():
        deleted_task=lb.get(i)
    
    deleted_task_withoutnumber=deleted_task.split()
    ToDoList.remove(deleted_task_withoutnumber[1])
   
    lb.delete(0, END)

    global count
    count=1
    for item in ToDoList:
        lb.insert(END, str(count)+". "+item)
        count+=1


root=Tk()
root.title('To Do list')
root.geometry('380x450')


e=Entry(root,width=50,borderwidth=5)
e.grid(row=0,column=0,padx=30,pady=30,columnspan=2)

btn_add=Button(root,text ='Add Task',padx=20,pady=20,command=addToList)
btn_del=Button(root,text ='Delete Task',padx=20,pady=20,command=deleteFromList)
btn_add.grid(row=1,column=0,padx=10,pady=10)
btn_del.grid(row=1,column=1,padx=10,pady=10)


lb = Listbox(
    root,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
    
)
lb.grid(row=2,column=0,columnspan=2,padx=20, pady=20)
for item in ToDoList:
    lb.insert(END, item)

root.mainloop()


