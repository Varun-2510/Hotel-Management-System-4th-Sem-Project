from tkinter import *
from tkinter import ttk
from PIL import Image , ImageTk
from tkinter import messagebox
from subprocess import call
import pymysql

root = Tk()

def add_employee():

    nam = name.get()
    ag = age.get()
    gen = r.get()
    job = combo.get()
    sal = salary.get()
    phn = phone.get()
    adh = aadhar.get()
    eml = email.get()

    try:

        connect_ = pymysql.connect(host = "localhost" , user = "root" ,
        password = "123456789" ,database = "hotel")

        cursor_ = connect_.cursor()
        cursor_.execute(f"insert into employee value {nam , ag , gen , job , sal , phn, adh , eml}")
            
        messagebox.showinfo("Succees" , "New Employee Added Successfully")

        connect_.commit()
        connect_.close()
        root.destroy()

    except Exception as e:

        messagebox.showerror("Error",f"{e}")


root.configure(bg = "white")
root.title("Add Employee")
root.minsize(900,675)
root.maxsize(900,675)
root.geometry("900x675+275+55")

img = Image.open("V:\\Hotel Management System\\icons\\Staff.jpg")
resized = img.resize((400,700), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(resized)
l1 = Label(root,image = photo,borderwidth=0).place(x = 500 , y = 0)

l2 = Label(root,text="ADD EMPLOYEE DETAILS" ,font = f"Tahoma 30" ,fg ="blue",
bg ="white").place(x=20,y=5)

name = StringVar()
age = StringVar()

l3 = Label(root,text="Name" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=20,y=85)

t1 = Entry(root , textvariable = name , font = "Tahoma 17",
border = 2).place(x = 180 , y = 88)

l4 = Label(root,text="Age" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=20,y=150)

t2 = Entry(root , textvariable = age , font = "Tahoma 17",
border = 2).place(x = 180 , y = 153)

l5 = Label(root,text="Gender" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=20,y=215)

r = StringVar()
r.set("None")

r1 = Radiobutton(root,text = "Male", font = "Tahoma 18",background="white",
padx = 25,value = "Male" , variable = r).place(x = 160 ,y = 215)

r2 = Radiobutton(root,text = "Female", font = "Tahoma 18",background="white",
padx = 20,value = "Female" , variable = r).place(x = 290 ,y = 215)

l6 = Label(root,text="Job" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=20,y=280)

job_list = ["Front Desk Clerks","Porters","Housekeeping","Kitchen Staff",
"Room Service","Waiter/Waitress","Manager","Accountant","Chef"]

combo = ttk.Combobox(root , value = job_list , font = "Tahoma 16",
background="white",foreground="black",state="readonly",width=22)

combo.set("Search")
combo.place(x = 179,y = 283)

l7 = Label(root,text="Salary" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=20,y=345)

salary = StringVar()

t3 = Entry(root , textvariable = salary , font = "Tahoma 17",
border = 2).place(x = 180 , y = 348)

l8 = Label(root,text="Phone" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=20,y=410)

phone = StringVar()

t4 = Entry(root , textvariable = phone , font = "Tahoma 17",
border = 2).place(x = 180 , y = 413)

l9 = Label(root,text="Aadhar" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=20,y=475)

aadhar = StringVar()

t5 = Entry(root , textvariable = aadhar , font = "Tahoma 17",
border = 2).place(x = 180 , y = 478)

l10 = Label(root,text="Email" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=20,y=540)

email = StringVar()

t6 = Entry(root , textvariable = email , font = "Tahoma 17",
border = 2).place(x = 180 , y = 543)

b1 = Button(root,bg = "black" , fg = "white" ,text = "Add" ,font="Tahoma 20",border = 2
,padx=50,cursor = "hand2",width = 11 , command = add_employee).place(x=175,y=600)


root.mainloop()