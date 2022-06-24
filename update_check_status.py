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

    name = combo_1.get()

    try:

        connect_ = pymysql.connect(host = "localhost" , user = "root" ,
        password = "123456789" ,database = "hotel")

        cursor_ = connect_.cursor()
        cursor_.execute("select * from customer where name = '" +name+ "'")
        res = cursor_.fetchall()

        for row in res:
            id.set(row[0])
            number.set(row[1])
            room_number.set(row[5])
            status.set(row[6])
            days.set(row[10])
            amount.set(row[7])

            day = row[10]  
            depo = row[7]  

        cursor_1 = connect_.cursor()
        cursor_1.execute("select * from room where room_number = '" +room_number.get()+ "'")
        res1 = cursor_1.fetchall()

        for r in res1:
            pass

            price = r[3]

        pending = (int(day) * int(price)) - int(depo)

        pending_amount.set(pending)

        connect_.commit()
        connect_.close()

    except Exception as e:

        messagebox.showerror("Error" , "Please Select Customer Name")

def update():
    
    name = combo_1.get()
    
    try:

        connect_ = pymysql.connect(host = "localhost" , user = "root" ,
        password = "123456789" ,database = "hotel")

        cursor_ = connect_.cursor()
        cursor_.execute(f"update customer set deposit = '"+amount.get()+"',id = '"+id.get()+"',number = '"+number.get()+"',days = '"+days.get()+"' where name = '"+name+"'")
                    
        messagebox.showinfo("Succees" , "Details Updated Successfully")

        connect_.commit()
        connect_.close()

    except Exception as e:

        messagebox.showerror("Error",f"{e}")

        connect_.commit()
        connect_.close()

    root.destroy()   
    call(["python" , "reception.py"])
    
    
root.configure(bg = "white")
root.title("Update Check Status")
root.minsize(1250,680)
root.maxsize(1250,680)
root.geometry("1250x680+70+52")

img = Image.open("V:\\Hotel Management System\\icons\\check_update_status.jpg")
resized = img.resize((615,725), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(resized)
l1 = Label(root,image = photo,borderwidth=0).place(x = 650 , y = 0)

l2 = Label(root,text="Check-In Details" ,font = f"Tahoma 30" ,fg ="blue",
bg ="white").place(x=165,y=0)

l3 = Label(root,text="Customer Name" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=35,y=70)

connect_ = pymysql.connect(host = "localhost" , user = "root" ,
password = "123456789" ,database = "hotel")

cur=connect_.cursor()
cur.execute("select * from customer where status = 'In' ")
res1 = cur.fetchall()
l = []

for i in res1:
    l.append(i[2])

combo_1 = ttk.Combobox(root, values = l,  font = "Tahoma 16",justify = CENTER,
background="white",foreground="black",width=22,state="readonly")

combo_1.set("Search")
combo_1.place(x = 330,y = 78)


l4 = Label(root,text="Customer Id" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=35,y=140)

id = StringVar()

t1 = Entry(root , textvariable = id , font = "Tahoma 17",justify = CENTER,
border = 2).place(x = 330 , y = 140)

l5 = Label(root,text="Id Number" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=35,y=205)

number = StringVar()

t2 = Entry(root , textvariable = number , font = "Tahoma 17",justify = CENTER,
border = 2).place(x = 330 , y = 205)

l6 = Label(root,text="Room Number" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=35,y=265)

room_number = StringVar()

t3 = Entry(root , textvariable = room_number , font = "Tahoma 17",state="readonly",
border = 2,justify = CENTER).place(x = 330 , y = 265)

l7 = Label(root,text="Check Status" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=35,y=330)

status = StringVar()

t4 = Entry(root , textvariable = status, font = "Tahoma 17",state="readonly",justify = CENTER,
border = 2).place(x = 330 , y = 330)

l8 = Label(root,text="Number of Days" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=35,y = 400)

days = StringVar()

t5 = Entry(root , textvariable = days, font = "Tahoma 17",justify = CENTER,
border = 2).place(x = 330 , y = 400)

l9 = Label(root,text="Amount Paid" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=35,y=470)

amount = StringVar()

t6 = Entry(root , textvariable = amount, font = "Tahoma 17",justify = CENTER,
border = 2).place(x = 330 , y = 470)

l10 = Label(root,text="Pending Amount" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=35,y=540)

pending_amount = StringVar()

t7 = Entry(root , textvariable = pending_amount, font = "Tahoma 17",state="readonly",
border = 2,justify = CENTER).place(x = 330 , y = 540)

b1 = Button(root,bg = "black" , fg = "white" ,text = "Check" ,
font="Tahoma 17",border = 2, padx=70,cursor = "hand2",width = 3 , command=check).place(x=30,y=620)

b2 = Button(root,bg = "black" , fg = "white" ,text = "Update" ,
font="Tahoma 17",border = 2, padx=70,cursor = "hand2",width = 3 , command = update).place(x=235,y=620)

b3 = Button(root,bg = "black" , fg = "white" ,text = "Back" ,
font="Tahoma 17",border = 2, padx=70,cursor = "hand2",width = 3 , command=back).place(x=440,y=620)

root.mainloop()
