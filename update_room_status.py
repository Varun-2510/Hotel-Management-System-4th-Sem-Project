from tkinter import *
from tkinter import ttk
from PIL import Image , ImageTk
from tkinter import messagebox
from subprocess import call
import pymysql

root = Tk()

def back():
    root.destroy()
    call(["python" , "reception.py"])

def check():

    room_number = combo_1.get()

    if(room_number == "Search"):
        messagebox.showerror("Error" , "Please Select Room Number")

    try:

        connect_ = pymysql.connect(host = "localhost" , user = "root" ,
        password = "123456789" ,database = "hotel")

        cursor_ = connect_.cursor()
        cursor_.execute("select * from room where room_number = '" +room_number+ "'")
        res = cursor_.fetchall()

        for row in res:
            available.set(row[1])
            status.set(row[2])
            price.set(row[3])
            bed_type.set(row[4])
            room_type.set(row[5])

        connect_.commit()
        connect_.close()

    except Exception as e:

        messagebox.showerror("Error",f"{e}")


def update():
    
    room_number = combo_1.get()
    
    try:

        connect_ = pymysql.connect(host = "localhost" , user = "root" ,
        password = "123456789" ,database = "hotel")

        cursor_ = connect_.cursor()
        cursor_.execute(f"update room set available = '"+available.get()+"',status = '"+status.get()+"', price = '"+price.get()+"',bed_type = '"+bed_type.get()+"',room_type = '"+room_type.get()+"' where room_number = '"+room_number+"'")

        messagebox.showinfo("Succees" , "Details Updated Successfully")

        connect_.commit()
        connect_.close()

    except Exception as e:
        messagebox.showerror("Error",f"{e}")

    root.destroy()   
    call(["python" , "reception.py"])

#---------------------------------------------------------------------------------------------    
    
root.configure(bg = "white")
root.title("Update Check Status")
root.minsize(1250,580)
root.maxsize(1250,580)
root.geometry("1250x580+75+100")

img = Image.open("V:\\Hotel Management System\\icons\\update_room.jpg")
resized = img.resize((600,720), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(resized)
l1 = Label(root,image = photo,borderwidth=0).place(x = 645 , y = -90)

l2 = Label(root,text="Room Status" ,font = f"Tahoma 30" ,fg ="blue",
bg ="white").place(x=165,y=0)

l3 = Label(root,text="Room Number" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=35,y=90)

connect_ = pymysql.connect(host = "localhost" , user = "root" ,
password = "123456789" ,database = "hotel")

cursor_ = connect_.cursor()
cursor_.execute("select room_number from room")
data = cursor_.fetchall()
connect_.close()

combo_1 = ttk.Combobox(root, value = data,  font = "Tahoma 16",justify = CENTER,
background="white",foreground="black",state="readonly",width=22)

combo_1.set("Search")
combo_1.place(x = 330,y = 98)

l4 = Label(root,text="Availability" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=35,y=160)

available = StringVar()

t1 = Entry(root , textvariable = available , font = "Tahoma 17",justify = CENTER,
border = 2).place(x = 330 , y = 160)

l5 = Label(root,text="Clean Status" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=35,y=225)

status = StringVar()

t2 = Entry(root , textvariable = status , font = "Tahoma 17",justify = CENTER,
border = 2).place(x = 330 , y = 225)

l6 = Label(root,text="Room Price" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=35,y=285)

price = StringVar()

t3 = Entry(root , textvariable = price , font = "Tahoma 17",justify = CENTER,
border = 2).place(x = 330 , y = 285)

l7 = Label(root,text="Bed Type" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=35,y=350)

bed_type = StringVar()

t4 = Entry(root , textvariable = bed_type, font = "Tahoma 17",justify = CENTER,
border = 2).place(x = 330 , y = 350)

l8 = Label(root,text="Room Type" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=35,y = 420)

room_type = StringVar()

t5 = Entry(root , textvariable = room_type, font = "Tahoma 17",justify = CENTER,
border = 2).place(x = 330 , y = 420)


b1 = Button(root,bg = "black" , fg = "white" ,text = "Check" ,
font="Tahoma 17",border = 2, padx=70,cursor = "hand2",width = 3 , command=check).place(x=30,y=500)

b2 = Button(root,bg = "black" , fg = "white" ,text = "Update" ,
font="Tahoma 17",border = 2, padx=70,cursor = "hand2",width = 3, command = update ).place(x=235,y=500)

b3 = Button(root,bg = "black" , fg = "white" ,text = "Back" ,
font="Tahoma 17",border = 2, padx=70,cursor = "hand2",width = 3 , command=back).place(x=440,y=500)

root.mainloop()
