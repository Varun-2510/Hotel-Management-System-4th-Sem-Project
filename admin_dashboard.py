from tkinter import *
from PIL import Image , ImageTk
from tkinter import messagebox
from subprocess import call

root = Tk()

def logout():
    messagebox.showinfo("Logout" , "Logout Succesfull")
    root.destroy()

def reception():
    call(["python" , "reception.py"])

def add_employee():
    call(["python" , "add_employee.py"])

def add_room():
    call(["python" , "add_room.py"])

def add_employee_id():
    call(["python" , "add_employee_id.py"])

root.configure(bg = "white")
root.title("Dashboard")
root.maxsize(1360,730)
root.minsize(1360,730)
root.geometry("1360x730+0+0")

menu_bar = Menu(root)

m1 = Menu(menu_bar , tearoff=0,background="white" ,foreground="black")
m1.add_command(label="Reception",font = "Tahoma 15",command = reception)

menu_bar.add_cascade(label="Hotel Management",menu=m1)

m2 = Menu(menu_bar , tearoff=0,background="white" ,foreground="black")

m2.add_command(label="Add Employee",font = "Tahoma 15",command = add_employee)
m2.add_separator()
m2.add_command(label="Add Room",font = "Tahoma 15",command = add_room)
m2.add_separator()
m2.add_command(label="Add Employee Id",font = "Tahoma 15",command=add_employee_id)

menu_bar.add_cascade(label="Admin",menu=m2)

menu_bar.add_command(label="Logout",command = logout)

root.config(menu = menu_bar)

img = Image.open("V:\\Hotel Management System\\icons\\background_1.jpg")
resized = img.resize((1360,730), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(resized)
l1 = Label(root,image = photo).pack()

root.mainloop()