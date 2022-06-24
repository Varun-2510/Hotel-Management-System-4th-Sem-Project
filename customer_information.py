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
    cursor_.execute("select * from customer")
    
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

tree["columns"] = ("id" , "number" , "name" ,"gender" ,"country" , "room_number",
"status" , "deposit" , "check_in_date" , "check_out_date" , "days")

tree.column("id" , width = 210 , minwidth = 210,anchor = CENTER)
tree.column("number" , width = 210 ,minwidth = 210, anchor = CENTER)
tree.column("name" , width = 210 ,minwidth = 210, anchor = CENTER)
tree.column("gender" , width = 210 ,minwidth = 210, anchor = CENTER)
tree.column("country" , width = 210 ,minwidth = 210, anchor = CENTER)
tree.column("room_number" , width = 207 ,minwidth = 207, anchor = CENTER)
tree.column("status" , width = 190 ,minwidth = 190, anchor = CENTER)
tree.column("deposit" , width = 200 ,minwidth = 200, anchor = CENTER)
tree.column("check_in_date" , width = 200 ,minwidth = 200, anchor = CENTER)
tree.column("check_out_date" , width = 200 ,minwidth = 200, anchor = CENTER)
tree.column("days" , width = 250 ,minwidth = 250, anchor = CENTER)

tree.heading("id" , text = "Document Type" , anchor = CENTER)
tree.heading("number" , text = "Number" , anchor = CENTER)
tree.heading("name" , text = "Name" , anchor = CENTER)
tree.heading("gender" , text = "Gender" , anchor = CENTER)
tree.heading("country" , text = "Country" , anchor = CENTER)
tree.heading("room_number" , text = "Room Number" , anchor = CENTER)
tree.heading("status" , text = "Checked Status" , anchor = CENTER)
tree.heading("deposit" , text = "Amount Paid" , anchor = CENTER)
tree.heading("check_in_date" , text = "Check-In Date" , anchor = CENTER)
tree.heading("check_out_date" , text = "Check-Out Date" , anchor = CENTER)
tree.heading("days" , text = "Number of Days" , anchor = CENTER)

i = 0

for row in cursor_:
    tree.insert('',i,values = (row[0] , row[1] , row[2] , row[3] , row[4] , row[5] 
    ,row[6] ,row[7] , row[8] , row[9] , row[10]))

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
,padx=70,pady = 5,cursor = "hand2" , command=back).place(x=570,y=620)


root.configure(bg = "white")
root.title("Customer Information")
root.minsize(1350,680)
root.maxsize(1350,680)
root.geometry("1350x680+5+55")

root.mainloop()