import tkinter
from tkinter import*
import mysql.connector
from tkinter import messagebox
root=tkinter.Tk()
root.title("NOBITA")
root.configure(bg="white")
#root.iconbitmap(r'mani.ico')
root.geometry('1366x768')


def insert():
    u=username.get()
    p=int(pin.get())
    con=mysql.connector.connect(host="localhost",user="root",password="vikash2005",database="skype")
    cur=con.cursor()
    cur.execute("insert into login values('%s','%d')"%(u,p))
    con.commit()
    messagebox.showinfo("LOGIN SUCCESFULLY","your email id has been logined")


def signin(): 
    username=username.get()
    pin=pin.get()


bg =PhotoImage(file="login.png")
img=Label(root,image=bg)
img.place(x=350,y=200)

frame=Frame(root,width=400,height=400,bg="white")
frame.place(x=700,y=250)

sign_in=Label(frame,text="Welcome to skype",fg="blue",bg="white",font=("Microsoft YaHei UI",23,"bold"))
sign_in.place(x=30,y=20)

def on_entry(e):
    username.delete(0,'end')

def on_leave(e):
    name=username.get()
    if name=='':
        username.insert(0,'gmail')

username= Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft YaHei UI",11))
username.place(x=30,y=90)
username.insert(0,"gmail")
username.bind("<FocusIn>",on_entry)
username.bind("<FocusOut>",on_leave)
username.get()

Frame(frame,width=295,height=2,bg="black").place(x=25,y=114)


def on_entry(e):
    pin.delete(0,'end')

def on_leave(e):
    name=pin.get()
    if name=='':
        pin.insert(0,'pin')


pin= Entry(frame,width=25,fg="black",border=0,bg="white",font=("Microsoft YaHei UI",11))
pin.place(x=30,y=150)
pin.insert(0,"Pin")
pin.bind("<FocusIn>",on_entry)
pin.bind("<FocusOut>",on_leave)
pin.get()



Frame(frame,width=295,height=2,bg="black").place(x=25,y=175)


Button (frame,width=40,pady=9,text="Login",bg="blue",fg="white",border=0,command=insert).place(x=30,y=205)

root.mainloop()
