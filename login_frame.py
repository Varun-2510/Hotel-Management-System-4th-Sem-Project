from tkinter import *
from PIL import Image , ImageTk
from subprocess import call

root = Tk()

def admin_frame():
    root.destroy()
    call(["python" , "login_admin.py"])

def employee_frame():
    root.destroy()
    call(["python" , "login_employee.py"])

root.configure(bg = "white")
root.title("Login Frame")
root.minsize(900,380)
root.maxsize(900,380)
root.geometry("900x400+280+140")

img = ImageTk.PhotoImage(file = "V:\\Hotel Management System\\icons\\login_frame.jpg")

can_widget = Canvas(root,bg="white",borderwidth=0)
can_widget.create_image(0,0,image = img)
can_widget.create_text(460,70 , text = "LOGIN",fill="white",font = "Tahoma 37")
can_widget.pack(fill="both" , expand = True)

b1 = Button(root,bg = "white" , fg = "black" ,text = "ADMIN" ,font="Tahoma 28"
,padx=80,borderwidth=2,command=admin_frame, cursor = "hand2").place(x=90,y=200)

b2 = Button(root,bg = "white" , fg = "black" ,text = "EMPLOYEE" ,font="Tahoma 28"
,padx=50,borderwidth=2,command=employee_frame, cursor = "hand2").place(x=520,y=200)

root.mainloop()