from tkinter import *
from PIL import Image , ImageTk
from tkinter import messagebox
import pymysql
from subprocess import call

root = Tk()

def employee_id():

    a = user_name.get()
    b = pass_word.get()

    if (a == "" and b == ""):
        messagebox.showerror("Error" , "Please Enter Username and Password")
    
    elif(b == ""):
        messagebox.showerror("Error" , "Please Enter Password")

    elif(a == ""):
        messagebox.showerror("Error" , "Please Enter Username")

    else:
        try:
            connect_ = pymysql.connect(host = "localhost" , user = "root" ,
            password = "123456789" ,database = "hotel")

            cursor_ = connect_.cursor()
            cursor_.execute(f"insert into employee_login value{a,b}")
            
            messagebox.showinfo("Succees" , "New Employee-Id Added Successfully")

            connect_.commit()
            connect_.close()
            root.destroy()

        except Exception as e:
            messagebox.showerror("Error",f"{e}")

def cancel():
    root.destroy()

root.configure(bg = "white")
root.title("Add Employee Id")
root.minsize(800,420)
root.maxsize(800,420)
root.geometry("800x420+325+125")

img = Image.open("V:\\Hotel Management System\\icons\\employee.jpg")
resized = img.resize((400,420), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(resized)
l1 = Label(root,image = photo,borderwidth=0).place(x = 450 , y = 0)

l2 = Label(root,text="ADD EMPLOYEE ID" ,font = f"Tahoma 30" ,fg ="blue",
bg ="white").place(x=40,y=10)

user_name = StringVar()
pass_word = StringVar()

l3 = Label(root,text="Username" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=20,y=120)

t1 = Entry(root , textvariable = user_name , font = "Tahoma 17",
border = 2).place(x = 175 , y = 123)

l4 = Label(root,text="Password" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=20,y=210)

t2 = Entry(root , textvariable = pass_word , font = "Tahoma 17",
border = 2).place(x = 175 , y = 213)

b1 = Button(root,bg = "black" , fg = "white" ,text = "Add" ,font="Tahoma 20",border = 2
,padx=60,cursor = "hand2", command = employee_id).place(x=30,y=310)

b2 = Button(root,bg = "black" , fg = "white" ,text = "Cancel" ,font="Tahoma 20",border = 2
,padx=50,cursor = "hand2",command = cancel).place(x=235,y=310)

root.mainloop()