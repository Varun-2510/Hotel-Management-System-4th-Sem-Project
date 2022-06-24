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
    cursor_.execute("select * from room")

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

tree["columns"] = ("room_number","available" , "status" ,"price" ,
"bed_type","room_type")

tree.column("room_number" , width = 210 , minwidth = 210,anchor = CENTER)
tree.column("available" , width = 210 ,minwidth = 210, anchor = CENTER)
tree.column("status" , width = 210 ,minwidth = 210, anchor = CENTER)
tree.column("price" , width = 210 ,minwidth = 210, anchor = CENTER)
tree.column("bed_type" , width = 210 ,minwidth = 210, anchor = CENTER)
tree.column("room_type" , width = 207 ,minwidth = 207, anchor = CENTER)

tree.heading("room_number" , text = "Room Number" , anchor = CENTER)
tree.heading("available" , text = "Availability" , anchor = CENTER)
tree.heading("status" , text = "Clean Status" , anchor = CENTER)
tree.heading("price" , text = "Room Price" , anchor = CENTER)
tree.heading("bed_type" , text = "Bed Type" , anchor = CENTER)
tree.heading("room_type" , text = "Room Type" , anchor = CENTER)
    
i = 0

for row in cursor_:
    tree.insert('',i,values = (row[0] , row[1] , row[2] , row[3] , row[4] , row[5]))

scroll_bar = ttk.Scrollbar(root)

scroll_bar.configure(command = tree.yview)
tree.configure(yscrollcommand = scroll_bar.set)
scroll_bar.pack(fill = Y , side = RIGHT )

tree.place(x = 2 ,height= 610 , width = 1260)

b1 = Button(root,bg = "black" , fg = "white" ,text = "Back" ,font="Tahoma 16",border = 2
,padx=70,pady = 5,cursor = "hand2" , command=back).place(x=560,y=615)


root.configure(bg = "white")
root.title("Room Information")
root.minsize(1280,670)
root.maxsize(1280,670)
root.geometry("1280x670+50+60")

root.mainloop()