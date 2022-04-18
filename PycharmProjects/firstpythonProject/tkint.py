import tkinter
from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()
root.geometry("350x420")
root.title("Register")
c = StringVar()
var1=IntVar()

lbl = Label(root,text="Student Registration",font="Ariel 16 bold").place(x=80,y=40)

lbl_1 = Label(root,text="Name").place(x=70,y=100)
lbl_2 = Label(root,text="Email").place(x=70,y=140)
lbl_3 = Label(root,text="Gender").place(x=70,y=180)
lbl_4 = Label(root,text="Country").place(x=70,y=220)
lbl_5 = Label(root,text="Course").place(x=70,y=260)
lbl_6 = Label(root,text="Password").place(x=70,y=300)

name=StringVar()
email=StringVar()
passwrd=StringVar()
var=IntVar()
var2=IntVar()

entry_1 = Entry(root,textvariable=name).place(x=150,y=100)
entry_2 = Entry(root,textvariable=email).place(x=150,y=140)
entry_3 = Entry(root,textvariable=passwrd,show='*').place(x=150,y=300)


radio = Radiobutton(root,text="Male",variable=var,value=1).place(x=150,y=180)
radio= Radiobutton(root,text="Female",variable=var,value=2).place(x=220,y=180)

list = ['India','Australia','Canada','Africa','France']
droplist = OptionMenu(root,c,*list)
droplist.config(width=15)
c.set('Select your country')
droplist.place(x=150,y=220)


check = Checkbutton(root,text="JAVA",variable=var1).place(x=150,y=260)
check_1 = Checkbutton(root,text="PYTHON",variable=var2).place(x=200,y=260)

def register_data():
    if name.get() == '' or email.get() == '' or passwrd.get == '':
        messagebox.showerror('Error',"All Fields are mandatory!")
    name1=name.get()
    email1=email.get()
    country=c.get()
    gender=var.get()
    course=var2.get()
    conn=sqlite3.connect('Registration.db')
    with conn:
        cursor=conn.cursor()
    cursor.execute('INSERT INTO Student(Name,Email,Country,Gender,Course) VALUES (?,?,?,?,?)',(name1,email1,country,gender,course))

    conn.commit()






btn = Button(root,text="Submit",command=register_data)
btn.place(x=150,y=330)
root = mainloop()