from tkinter import *
from PIL import Image , ImageTk
from tkinter import messagebox
import pymysql
from subprocess import call

root = Tk()

def login_frame():
    root.destroy()
    call(["python" , "login_frame.py"])

def login():
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
            cursor_.execute("select * from login where username = %s and password = %s",(a,b))

            data = cursor_.fetchone()
            
            if (data == None):
                messagebox.showerror("Error" , "Invalid Username and Password")

            else:
                messagebox.showinfo("Succees" , "Login Successful")
                root.destroy()
                call(["python" , "admin_dashboard.py"])
                connect_.close()

        except Exception as e:
            messagebox.showerror("Error",f"{e}")

root.configure(bg = "white")
root.title("Admin Login")
root.minsize(900,400)
root.maxsize(900,400)
root.geometry("900x400+280+140")

img = Image.open("V:\\Hotel Management System\\icons\\login.png")
resized = img.resize((400,390), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(resized)

l1 = Label(root,image = photo,borderwidth=0).place(x=490)

l2 = Label(root,text="Admin Login" ,font = f"Tahoma 30" ,fg ="blue",
bg ="white").place(x=125,y=20)

user_name = StringVar()
pass_word = StringVar()

l3 = Label(root,text="Username" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=30,y=125)

t1 = Entry(root , textvariable = user_name , font = "Tahoma 17",
borderwidth = 2).place(x = 190 , y = 130)

l4 = Label(root,text="Password" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=30,y=210)

t2 = Entry(root , textvariable = pass_word , font = "Tahoma 17",
borderwidth = 2 , show = "*").place(x = 190 , y = 215)

b1 = Button(root,bg = "black" , fg = "white" ,text = "Login" ,font="Tahoma 20"
,padx=50,borderwidth=2,command = login , cursor = "hand2").place(x=45,y=310)

b2 = Button(root,bg = "black" , fg = "white" ,text = "Cancel" ,font="Tahoma 20" 
,padx=40,borderwidth=2,command=login_frame, cursor = "hand2").place(x=260,y=310)

root.mainloop()