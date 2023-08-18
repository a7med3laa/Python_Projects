from tkinter import *

master = Tk()

# set the title of GUI window
master.title("Simple Security App")




# Define encrypt_caesar function that take massage and 
# shift amount to encrypt message
def encrypt_caesar(msg,shift):
    encrypted_msg=''
    # for every char in message gets its index in alphabets then 
    # apply encryption equation and add it to encrypted_msg
    for i in msg:
        char_index=alpha.index(i)
        e=(char_index + shift) % 26
        encrypted_msg+=alpha[e]
    return encrypted_msg


# Define decrypt_caesar function that take cipher and 
# shift amount to decrypt message
def decrypt_caesar(encrypted_msg,shift):
    msg=''
    # for every char in encrypted_msg gets its index then 
    # apply decryption equation and add it to msg
    for i in encrypted_msg:
        char_index=alpha.index(i)
        d=(char_index - shift) % 26
        msg+=alpha[d]
    return msg

# Define encrypt_affine function that take massage and encrypt it
def encrypt_affine(msg):
    encrypted_msg=''
    # for every char in message gets its index in alphabets then 
    # apply encryption equation and add it to encrypted_msg
    for i in msg:
        char_index=alpha.index(i)
        e=(5*char_index + 8) % 26
        encrypted_msg+=alpha[e]
    return encrypted_msg

def decrypt_affine (encrypted_msg):
    msg=''
    # for every char in encrypted_msg gets its index then 
    # apply decryption equation and add it to msg
    for i in encrypted_msg:
        char_index=alpha.index(i)
        d=(21*(char_index - 8)) % 26
        msg+=alpha[d]
    return msg

#define encrypt function
def encrypt ():
    global alpha 
    alpha= 'abcdefghijklmnopqrstuvwxyz'
    if v.get()== 1: # if user choose caesar cipher
        enc=encrypt_caesar(e.get(),3)
        o.delete(0,END)
        o.insert(0,enc)
    elif v.get()==2:# if user choose affine cipher
        enc=encrypt_affine(e.get())
        o.delete(0,END)
        o.insert(0,enc)

#define decrypt function
def decrypt():
    if v.get()== 1: # if user choose caesar cipher
        dec=decrypt_caesar(e.get(),3)
        o.delete(0,END)
        o.insert(0, dec)
    elif v.get()== 2: # if user choose affine cipher
        dec=decrypt_affine(e.get())
        o.delete(0,END)
        o.insert(0, dec)

#define clear function
def button_clear():
    e.delete(0,END)
    o.delete(0,END)

lb_text=Label(master,text="Enter your text: ")
lb_text.grid(row=0,column=0,columnspan=2,padx=10,pady=10)
lb_msg=Label(master,text="Convert To: ")
lb_msg.grid(row=2,column=0,columnspan=2,padx=10,pady=10)
lb_res=Label(master,text="Result : ")
lb_res.grid(row=6,column=0,columnspan=2,padx=10,pady=10)


e=Entry(master,width=30,borderwidth=5)
e.grid(row=1,column=0,columnspan=2,padx=20,pady=20)

o=Entry(master,width=30,borderwidth=5)
o.grid(row=7,column=0,columnspan=2,padx=20,pady=20)

btn_En=Button(master,text="Encrypt",padx=10,pady=10,command=encrypt)
btn_En.grid(row=4,column=0,padx=10,pady=10)
btn_De=Button(master,text="Decrypt",padx=10,pady=10,command=decrypt)
btn_De.grid(row=4,column=1,padx=10,pady=10)
btn_clear=Button(master,text="Clear",padx=10,pady=10,command=button_clear)
btn_clear.grid(row=5,column=0,columnspan=2,padx=10,pady=10)

# Tkinter string variable
# able to store any string value
v = IntVar()
r1=Radiobutton(master, text="Caesar Cipher", variable=v, value=1)
r2=Radiobutton(master, text="Affine Cipher", variable=v, value=2)
r1.grid(row=3,column=0,padx=10,pady=10)
r2.grid(row=3,column=1,padx=10,pady=10)

mainloop()