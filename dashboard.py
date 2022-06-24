from tkinter import *
from PIL import Image , ImageTk
from subprocess import call

def login_frame():
    root.destroy()
    call(["python" , "login_frame.py"])

root = Tk()

root.configure(bg = "white")
root.title("Dashboard")
root.minsize(1365,730)
root.geometry("1365x730+0+0")

img = ImageTk.PhotoImage(file = "V:\\Hotel Management System\\icons\\g1.jpeg")

can_widget = Canvas(root,bg="white",borderwidth=0)
can_widget.create_image(690,340,image = img)
can_widget.pack(fill="both" , expand = True)

b1 = Button(root,bg = "black" , fg = "white" ,text = "Next" ,font="Tahoma 18"
,padx=30,borderwidth=2,command=login_frame, cursor = "hand2").place(x=1190,y=660)

root.mainloop()