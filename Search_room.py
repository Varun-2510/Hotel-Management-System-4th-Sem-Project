from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
from subprocess import call

root = Tk()

def back():
    root.destroy()
    call(["python" , "reception.py"])

def load_data():
        
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

    connect_ = pymysql.connect(host = "localhost" , user = "root" ,
    password = "123456789" ,database = "hotel")

    cursor_ = connect_.cursor()
    if(j.get() == 1):
        cursor_.execute("select * from room where available = 'Available' and bed_type = '"+combo.get()+"'")
    else:
        cursor_.execute("select * from room where bed_type = '"+combo.get()+"'")
         
    for row in cursor_:
        tree.insert('',i,values = (row[0] , row[1] , row[2] , row[3] , row[4] , row[5]))

    tree.place(x = 2 ,height= 500 , width = 1270 , y = 110)


# --------------------------------------------------------------------------black
l1 = Label(root,text="Room Bed Type" ,font = f"Tahoma 25" ,fg ="black",
bg ="white").place(x=120,y=40)

bed_type = ["Single Bed" , "Double Bed" , "Triple Bed"]

combo = ttk.Combobox(root , value = bed_type , font = "Tahoma 16",justify = CENTER,
background="white",foreground="black",width=22)

combo.set("Search")
combo.place(x = 400,y = 48)

j = IntVar()
c = Checkbutton(root , text = "Display Available" , font = "Tahoma 25",fg ="black",
bg ="white" , variable = j , command=load_data).place(x = 860 , y = 35)

b1 = Button(root,bg = "black" , fg = "white" ,text = "Back" ,font="Tahoma 16",border = 2
,padx=60,cursor = "hand2" , command=back).place(x=660,y=615)

b2 = Button(root,bg = "black" , fg = "white" ,text = "Load Data" ,font="Tahoma 16",border = 2
,padx=50,cursor = "hand2", command=load_data).place(x=380,y=615)

root.configure(bg = "white")
root.title("Search Room")
root.minsize(1280,670)
root.maxsize(1280,670)
root.geometry("1280x670+50+60")

root.mainloop()