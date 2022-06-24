from tkinter import *
from tkinter import ttk
from PIL import Image , ImageTk
from tkinter import messagebox
from subprocess import call
import pymysql

root = Tk()

def add_room():

    room_num = room_number.get()
    room_avl = c1.get()
    clean_stat = c2.get()
    amount = price.get()
    bed_ty =  c3.get()
    room_ty = c4.get()

    try:

        connect_ = pymysql.connect(host = "localhost" , user = "root" ,
        password = "123456789" ,database = "hotel")

        cursor_ = connect_.cursor()
        cursor_.execute(f"insert into room value {room_num,room_avl,clean_stat,amount,bed_ty,room_ty}")
            
        messagebox.showinfo("Succees" , "New Room Added Successfully")

        connect_.commit()
        connect_.close()
        root.destroy()

    except Exception as e:

        messagebox.showerror("Error",f"{e}")

def cancel():
    root.destroy()

root.configure(bg = "white")
root.title("Add Room")
root.minsize(900,650)
root.maxsize(900,650)
root.geometry("900x650+280+65")

img = Image.open("V:\\Hotel Management System\\icons\\room.jpg")
resized = img.resize((410,650), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(resized)
l1 = Label(root,image = photo,borderwidth=0).place(x = 490 , y = 0)

l2 = Label(root,text="ADD ROOM DETAILS" ,font = f"Tahoma 30" ,fg ="blue",
bg ="white").place(x=40,y=10)

l3 = Label(root,text="Room Number" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=10,y=95)

room_number = StringVar()

t1 = Entry(root , textvariable = room_number, font = "Tahoma 17",
border = 2).place(x = 215 , y = 100)

l4 = Label(root,text="Room Available" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=10,y=170)

room_available = ["Available" ,"Occupied"]

c1 = ttk.Combobox(root , value = room_available , font = "Tahoma 16",
background="white",foreground="black",state="readonly",width=22)

c1.set("Search")
c1.place(x = 215,y = 175)

l5 = Label(root,text="Cleaning Status" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=10,y=245)

clean_status = ["Cleaned" ,"Dirty"]

c2 = ttk.Combobox(root , value = clean_status , font = "Tahoma 16",
background="white",foreground="black",state="readonly",width=22)

c2.set("Search")
c2.place(x = 215,y = 250)

l6 = Label(root,text="Price" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=10,y=320)

price = StringVar()

t2 = Entry(root , textvariable = price, font = "Tahoma 17",
border = 2).place(x = 215 , y = 325)

l7 = Label(root,text="Bed Type" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=10,y=395)

bed_type = ["Single Bed" ,"Double Bed" , "Triple Bed"]

c3 = ttk.Combobox(root , value = bed_type , font = "Tahoma 16",
background="white",foreground="black",state="readonly",width=22)

c3.set("Search")
c3.place(x = 215,y = 400)

l8 = Label(root,text="Room Type" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=10,y=470)

room_type = ["AC" ,"Non AC"]

c4 = ttk.Combobox(root , value = room_type , font = "Tahoma 16",
background="white",foreground="black",state="readonly",width=22)

c4.set("Search")
c4.place(x = 215,y = 475)

b1 = Button(root,bg = "black" , fg = "white" ,text = "Add Room" ,font="Tahoma 20",border = 2
,padx=40,cursor = "hand2" , command = add_room).place(x=20,y=560)

b2 = Button(root,bg = "black" , fg = "white" ,text = "Cancel" ,font="Tahoma 20",border = 2
,padx=50,cursor = "hand2" , command = cancel).place(x=270,y=560)

root.mainloop()