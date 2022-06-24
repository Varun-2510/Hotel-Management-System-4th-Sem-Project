from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
from subprocess import call

root = Tk()

def back():
    root.destroy()
    call(["python" , "reception.py"])

try:
    connect_ = pymysql.connect(host = "localhost" , user = "root" ,
    password = "123456789" ,database = "hotel")

    cursor_ = connect_.cursor()
    cursor_.execute("select * from department")

except Exception as e:
    messagebox.showerror("Error",f"{e}")

# ------------------------------------------------------------------------------
s = ttk.Style(root)

s.theme_use("winnative")
s.configure("." , font = ("Tahoma" , 18))
s.configure("Treeview.Heading" , foreground = "blue" , font = "Tahoma 20" , background = "white")
s.configure("Treeview" , background = "white" , foreground = "black",
rowheight = 40)
s.map("Treeview" , background = [("selected" , "blue")])

tree = ttk.Treeview(root)

tree["show"] = "headings" 

tree["columns"] = ("dept" , "budget")

tree.column("dept" , width = 210 , minwidth = 210,anchor = CENTER)
tree.column("budget" , width = 210 ,minwidth = 210, anchor = CENTER)


tree.heading("dept" , text = "Department" , anchor = CENTER)
tree.heading("budget" , text = "Budget" , anchor = CENTER)

i = 0

for row in cursor_:
    tree.insert('',i,values = (row[0] , row[1]))

scroll_bar = ttk.Scrollbar(root)

scroll_bar.configure(command = tree.yview)
tree.configure(yscrollcommand = scroll_bar.set)
scroll_bar.pack(fill = Y , side = RIGHT )

tree.place(x = 2 ,height= 410 , width = 1260)

b1 = Button(root,bg = "black" , fg = "white" ,text = "Back" ,font="Tahoma 16",border = 2
,padx=70,cursor = "hand2" , command=back).place(x=540,y=420)


root.configure(bg = "white")
root.title("Department")
root.minsize(1280,480)
root.maxsize(1280,480)
root.geometry("1280x480+50+60")

root.mainloop()