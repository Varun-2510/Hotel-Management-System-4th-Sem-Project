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
    cursor_.execute("select * from employee")
    
except Exception as e:
    messagebox.showerror("Error",f"{e}")

# ------------------------------------------------------------------------------
s = ttk.Style(root)

s.theme_use("winnative")
s.configure("." , font = ("Tahoma" , 16))
s.configure("Treeview.Heading" , foreground = "blue" , font = "Tahoma 20" , background = "white")
s.configure("Treeview" , background = "white" , foreground = "black",
rowheight = 40)
s.map("Treeview" , background = [("selected" , "blue")])

tree = ttk.Treeview(root)

tree["show"] = "headings" 

tree["columns"] = ("name" , "age" , "gender" , "job" , "salary" , "phone",
"aadhar","email")

tree.column("name" , width = 210 , minwidth = 210,anchor = CENTER)
tree.column("age" , width = 210 ,minwidth = 210, anchor = CENTER)
tree.column("gender" , width = 210 ,minwidth = 210, anchor = CENTER)
tree.column("job" , width = 210 ,minwidth = 210, anchor = CENTER)
tree.column("salary" , width = 210 ,minwidth = 210, anchor = CENTER)
tree.column("phone" , width = 207 ,minwidth = 207, anchor = CENTER)
tree.column("aadhar" , width = 190 ,minwidth = 190, anchor = CENTER)
tree.column("email" , width = 300 ,minwidth = 300, anchor = CENTER)

tree.heading("name" , text = "Name" , anchor = CENTER)
tree.heading("age" , text = "Age" , anchor = CENTER)
tree.heading("gender" , text = "Gender" , anchor = CENTER)
tree.heading("job" , text = "Department" , anchor = CENTER)
tree.heading("salary" , text = "Salary" , anchor = CENTER)
tree.heading("phone" , text = "Phone" , anchor = CENTER)
tree.heading("aadhar" , text = "Aadhar" , anchor = CENTER)
tree.heading("email" , text = "Email" , anchor = CENTER)
    
i = 0

for row in cursor_:
    tree.insert('',i,values = (row[0] , row[1] , row[2] , row[3] , row[4] , row[5] 
    ,row[6] ,row[7]))

scroll_bar = ttk.Scrollbar(tree)

scroll_bar.configure(command = tree.yview)
tree.configure(yscrollcommand = scroll_bar.set)
scroll_bar.pack(fill = Y , side = RIGHT )

scroll_bar_1 = ttk.Scrollbar(tree, orient = "horizontal")

scroll_bar_1.configure(command = tree.xview)
tree.configure(xscrollcommand = scroll_bar_1.set)
scroll_bar_1.pack(fill = X , side = BOTTOM )

tree.place(height= 610 , width = 1350)

b1 = Button(root,bg = "black" , fg = "white" ,text = "Back" ,font="Tahoma 16",border = 2
,padx=70,pady= 5,cursor = "hand2" , command=back).place(x=570,y=620)


root.configure(bg = "white")
root.title("Employee Information")
root.minsize(1350,680)
root.maxsize(1350,680)
root.geometry("1350x680+5+55")

root.mainloop()