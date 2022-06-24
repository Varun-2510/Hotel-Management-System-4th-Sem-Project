from tkinter import *
from tkinter import ttk
from PIL import Image , ImageTk
from tkinter import messagebox
from subprocess import call
import pymysql
import time

root = Tk()

def back():
    root.destroy()
    call(["python" , "reception.py"])

def add_customer():

    id = combo.get()
    num = number.get()
    nam = name.get()
    gender = r.get()
    coun = country.get()
    alloc_room_num = combo_1.get()
    stat = status.get()
    date_ = t
    num_of_days = n_days.get()
    depo = deposit.get()

    try:

        connect_ = pymysql.connect(host = "localhost" , user = "root" ,
        password = "123456789" ,database = "hotel")

        cursor_ = connect_.cursor()
        cursor_.execute(f"insert into customer (id,number,name,gender,country,room_number,status,deposit,days) values ( '"+id+"', '"+num+"', '"+nam+"','"+gender+"', '"+coun+"', '"+alloc_room_num+"','"+stat+"', '"+depo+"','"+num_of_days+"')")
        cursor_.execute(f"update room set available = 'Occupied' where room_number = '"+alloc_room_num+"'")
        cursor_.execute("update customer set check_in_date = '"+date_+"' where name = '"+nam+"'")

        messagebox.showinfo("Succees" , "New Customer Added Successfully")

        connect_.commit()
        connect_.close()

        root.destroy()
        call(["python" , "reception.py"])
        
    except Exception as e:

        messagebox.showerror("Error",f"{e}")


    
root.configure(bg = "white")
root.title("Customer Form")
root.minsize(1100,680)
root.maxsize(1100,680)
root.geometry("1100x680+200+52")

img = Image.open("V:\\Hotel Management System\\icons\\customer.jpg")
resized = img.resize((450,670), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(resized)
l1 = Label(root,image = photo,borderwidth=0).place(x = 690 , y = 0)

l2 = Label(root,text="New Customer Form" ,font = f"Tahoma 30" ,fg ="blue",
bg ="white").place(x=165,y=0)

l3 = Label(root,text="ID" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=60,y=70)

id_details = ["Aadhar Card " , "Passport" , "Voter-id Card", "Pan Card" ,"Driving License"]

combo = ttk.Combobox(root , value = id_details , font = "Tahoma 16",justify = CENTER,
background="white",foreground="black",state="readonly",width=22)

combo.set("Search")
combo.place(x = 420,y = 70)

l4 = Label(root,text="Number" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=60,y=120)

number = StringVar()

t1 = Entry(root , textvariable = number , font = "Tahoma 17",
border = 2).place(x = 420 , y = 120)

l5 = Label(root,text="Name" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=60,y=170)

name = StringVar()

t2 = Entry(root , textvariable = name , font = "Tahoma 17",
border = 2).place(x = 420 , y = 170)

l6 = Label(root,text="Gender" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=60,y=220)

r = StringVar()
r.set("None")

r1 = Radiobutton(root,text = "Male", font = "Tahoma 18",background="white",
padx = 25,value = "Male" , variable = r).place(x = 400 ,y = 220)

r2 = Radiobutton(root,text = "Female", font = "Tahoma 18",background="white",
padx = 20,value = "Female" , variable = r).place(x = 540 ,y = 220)

l7 = Label(root,text="Country" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=60,y=270)

country = StringVar()

t3 = Entry(root , textvariable = country , font = "Tahoma 17",
border = 2).place(x = 420 , y = 270)

l8 = Label(root,text="Allocated Room Number" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=60,y=320)

connect_ = pymysql.connect(host = "localhost" , user = "root" ,
password = "123456789" ,database = "hotel")

cursor_ = connect_.cursor()
cursor_.execute("select room_number from room where available = 'Available'")
data = cursor_.fetchall()

connect_.close()

combo_1 = ttk.Combobox(root, value = data,  font = "Tahoma 16",justify = CENTER,
background="white",foreground="black",state="readonly",width=22)

combo_1.set("Search")
combo_1.place(x = 420,y = 325)

l9 = Label(root,text="Checked In Status" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=60,y=380)

status = StringVar()

t4 = Entry(root , textvariable = status, font = "Tahoma 17",
border = 2).place(x = 420 , y = 380)

l10 = Label(root,text="Checked In Date" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=60,y=440)

t = time.strftime('%Y / %m / %d',time.localtime())

time_ = StringVar(value = t)

t5 = Entry(root , font = "Tahoma 17", textvariable = time_ ,state="readonly",justify = CENTER,
border = 2).place(x = 420 , y = 440)

l11 = Label(root,text="Number of Days" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=60,y=500)

n_days = StringVar()

t6 = Entry(root , font = "Tahoma 17", textvariable = n_days,
border = 2).place(x = 420 , y = 500)

l12 = Label(root,text="Deposit" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=60,y=560)

deposit = StringVar()

t7 = Entry(root , font = "Tahoma 17", textvariable = deposit,
border = 2).place(x = 420 , y = 560)

b1 = Button(root,bg = "black" , fg = "white" ,text = "Add Customer" ,
font="Tahoma 17",border = 2, padx=60,cursor = "hand2",width = 11,command = add_customer).place(x=110,y=620)

b2 = Button(root,bg = "black" , fg = "white" ,text = "Back" ,font="Tahoma 17",border = 2,
 padx=50,cursor = "hand2",width = 11,command = back).place(x=440,y=620)

root.mainloop()