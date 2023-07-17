'''
#creating a window 

from tkinter import * #package for GUI
root=Tk()
root.geometry("400x400")
root.title("My Window")
root.config(background="red")
root.mainloop()

#creating frame:

from tkinter import *
root=Tk()
root.geometry("400x400")
root.title("My Window")
f=Frame(root,width=200,height=200,bg="red")
f.pack()
f1=Frame(root,width=200,height=200,bg="yellow")
f1.pack(anchor='w')
root.mainloop()

#UI widgets:

from tkinter import *
root=Tk()
root.geometry("400x400")
root.title("My Window")
l=Label(root,text="Hello World",bg="blue",fg="green")
l.pack(side="left",anchor='s')
root.mainloop()

#button

from tkinter import *
root=Tk()
root.geometry("400x400")
root.title("My window")
def button_click():
    print("button clicked")
b=Button(root,text="click Here!",command=button_click,bg="red")
b.pack()
root.mainloop()


#example (changing the text of lable dynamically)

from tkinter import *
root=Tk()
root.geometry("400x400")
root.title("My Window")
v=StringVar() #used for store/retrieve the values of UI widgets based on str.(Intvar(),#Floatvar(),BoolVar())
def get_label():
    print(v.get())
def set_label():
    v.set("welcome to python")
b=Button(root,text="get",command=get_label,bg="red")
b.pack()
b1=Button(root,text="set",command=set_label,bg="red")
b1.pack()
l=Label(root,textvariable=v,bg="red",fg="white")
v.set("Hello World")
l.pack()
root.mainloop()

#Entry- input field. used for store and retrieve text.
example

from tkinter import *
root=Tk()
root.geometry("400x400")
root.title("My window")
def get_entry():
    print("Welcome:",e.get())
e=Entry(root)
e.insert(0,"Hello")
e.pack()
b=Button(root,text="get",command=get_entry,bg="red")
b.pack()
root.mainloop()

#text -multiline input field

from tkinter import *
root=Tk()
root.geometry("400x400")
root.title("Text example")
def write_data():
    f=open("guitext.txt","w")
    f.write(t.get(0.0,END))
    f.flush()
    f.close()
def read_data():
    t.delete(0.0, END)
    f=open("guitext.txt","r")
    data=f.read()
    t.insert(0.0, data)
    f.close()

t=Text(root,width=25,height=5)
t.pack()
b1=Button(root,text="write",command=write_data)
b1.pack()
b2=Button(root,text="read",command=read_data)
b2.pack()
root.mainloop()


#List - shows multipleselect#

from tkinter import *
root=Tk()
root.geometry("400x400")
root.title("Text Example")
l=Listbox(root)
l.pack()
l.insert(END,"CSE")
for i in ["ECE","EEE","MECH"]:
    l.insert(END,i)
def select():
    e.delete(0,END)
    e.insert(0,l.get(l.curselection()))
e=Entry(root)
e.pack()
b1=Button(root,text="select",command=select)
b1.pack()
root.mainloop()



#combobox - drop down list#

import tkinter as tk
from tkinter import ttk, StringVar
root=tk.Tk()
root.geometry("400x400")
root.title("Text Example")
ll=ttk.Label(root,text="Select Day")
ll.pack()
day=StringVar()
days=ttk.Combobox(root,textvariable=day)
days['values']=('sun','mon','tue','wed','thu','fri','sat')
days.current(3)
days.pack()
def select():
    e.delete(0,tk.END)
    e.insert(0,day.get())
e=ttk.Entry(root)
e.pack()
b1=ttk.Button(root,text="Choose",command=select)
b1.pack()
root.mainloop()


#checkbutton#

from tkinter import *
root=Tk()
root.geometry("400x400")
root.title("Text Example")
c1=IntVar()
c2=IntVar()
e=Entry(root)
e.pack()
def select():
    if c1.get()==1:
        e.insert(0, "B.E")
    if c2.get()==1:
        e.insert(0, "M.E")

cb1=Checkbutton(root,variable=c1,command=select,text="B.E")
cb1.pack()
cb2=Checkbutton(root,variable=c2,command=select,text="M.E")
cb2.pack()
root.mainloop()
'''

#RadioButton
from tkinter import *
root=Tk()
root.geometry("400x400")
root.title("Text Example")
gen=StringVar()
e=Entry(root)
e.pack()
def select():
    e.delete(0, END)
    e.insert(0,gen.get())
rb1=Radiobutton(root,text="Male",variable=gen,value="male",command=select)
rb1.pack()
rb2=Radiobutton(root,text="Female",variable=gen,value="female",command=select)
rb2.pack()
root.mainloop()
from tkinter import*
root=Tk()
root.geometry("400x400")
root.title("Text Example")
e=Entry(root)
e.pack()
def new():
    e.delete(0, END)
    e.insert(0, "NEW")
def open():
    e.delete(0, END)
    e.insert(0, "open")

menubar=Menu(root)
filemenu=Menu(menubar)
filemenu.add_command(label="New",command=new)
filemenu.add_command(label="open",command=open)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=root.destroy)
menubar.add_cascade(label="File",menu=filemenu)

submenu=Menu(filemenu)
submenu.add_command(label="Exit",command=root.destroy)
filemenu.add_cascade(label="Recent",menu=submenu)

root.config(menu=menubar)
root.mainloop()








