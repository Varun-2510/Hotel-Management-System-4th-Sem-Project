from tkinter import *
from PIL import Image , ImageTk
from subprocess import call

root = Tk()

def room_information():
    root.destroy()
    call(["python" , "room_information.py"])

def employee_information():
    root.destroy()
    call(["python" , "employee_information.py"])


def customer_information():
    root.destroy()
    call(["python" , "customer_information.py"])

def manager_information():
    root.destroy()
    call(["python" , "manager_information.py"])

def department():
    root.destroy()
    call(["python" , "department.py"])

def customer():
    root.destroy()
    call(["python" , "customer_form.py"])

def update_check_status():
    root.destroy()
    call(["python" , "update_check_status.py"])

def update_room_status():
    root.destroy()
    call(["python" , "update_room_status.py"])

def search_room():
    root.destroy()
    call(["python" , "Search_room.py"])

def check_out():
    root.destroy()
    call(["python" , "check_out.py"])

root.configure(bg = "white")
root.title("Reception")
root.minsize(890,675)
root.maxsize(890,675)
root.geometry("890x675+290+55")

img = Image.open("V:\\Hotel Management System\\icons\\Reception.jpg")
resized = img.resize((680,750), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(resized)
l1 = Label(root,image = photo,borderwidth=0).place(x = 260 , y = 0)

b1 = Button(root,bg = "white" , fg = "black" ,text = "New Customer Form" ,font="Tahoma 18"
,padx=20,borderwidth=3,border = 2, cursor = "hand2" , command = customer).place(x=10,y=10)

b2 = Button(root,bg = "white" , fg = "black" ,text = "Room Information" ,font="Tahoma 18"
,padx=33,borderwidth=3,border = 2, cursor = "hand2",command = room_information).place(x=10,y=75)

b3 = Button(root,bg = "white" , fg = "black" ,text = "Department" ,font="Tahoma 18"
,padx=67,borderwidth=3,border = 2, cursor = "hand2",command = department).place(x=10,y=140)

b4 = Button(root,bg = "white" , fg = "black" ,text = "Employee Information" ,font="Tahoma 18"
,padx=13,borderwidth=3,border = 2, cursor = "hand2", command = employee_information).place(x=10,y=205)

b5 = Button(root,bg = "white" , fg = "black" ,text = "Customer Information" ,font="Tahoma 18"
,padx=13,borderwidth=3,border = 2, cursor = "hand2", command = customer_information).place(x=10,y=270)

b6 = Button(root,bg = "white" , fg = "black" ,text = "Manager Information" ,font="Tahoma 18"
,padx=18,borderwidth=3,border = 2, cursor = "hand2", command = manager_information).place(x=10,y=335)

b7 = Button(root,bg = "white" , fg = "black" ,text = "Check Out" ,font="Tahoma 18"
,padx=76,borderwidth=3,border = 2, cursor = "hand2" , command = check_out).place(x=10,y=400)

b8 = Button(root,bg = "white" , fg = "black" ,text = "Update Check Status" ,font="Tahoma 18"
,padx=20,borderwidth=3,border = 2, cursor = "hand2", command = update_check_status).place(x=10,y=465)

b9 = Button(root,bg = "white" , fg = "black" ,text = "Update Room Status" ,font="Tahoma 18"
,padx=20,borderwidth=3,border = 2, cursor = "hand2", command = update_room_status).place(x=10,y=530)

b10 = Button(root,bg = "white" , fg = "black" ,text = "Search Room" ,font="Tahoma 18"
,padx=59,borderwidth=3,border = 2, cursor = "hand2", command = search_room).place(x=10,y=595)

root.mainloop()