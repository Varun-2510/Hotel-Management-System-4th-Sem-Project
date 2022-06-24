
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from subprocess import call
import pymysql
import time
import qrcode
from PIL import Image , ImageTk
from resizeimage import resizeimage
from fpdf import FPDF
from pdf_mail import sendpdf

root = Tk()

def back():
    root.destroy()
    call(["python" , "reception.py"])
    
#--------------------------------------------------------------------------------------------- 

def qr():

    name = combo_1.get()

    connect_ = pymysql.connect(host = "localhost" , user = "root" ,
    password = "123456789" ,database = "hotel")

    cursor_ = connect_.cursor()
    cursor_.execute("select * from customer where name = '" +name+ "'")
    res = cursor_.fetchall()

    for row in res:
        id.set(row[0])
        number.set(row[1])
        room_number.set(row[5])

        day = row[10]  
        depo = row[7]  

    cursor_1 = connect_.cursor()
    cursor_1.execute("select * from room where room_number = '" +room_number.get()+ "'")
    res1 = cursor_1.fetchall()

    for r in res1:
        bed_type.set(r[4])
        room_type.set(r[5])

        price = r[3]

    pending = (int(day) * int(price)) - int(depo)

    pending_amount.set(pending)

    connect_.commit()
    connect_.close()

    s = pending_amount.get()

    if(int(s) == 0):

        qr_data = (f" ================== Hotel Sunshine ================ \nCustomer Name:  {combo_1.get()}\nId Number:  {number.get()}\nRoom Number:  {room_number.get()}\nBed Type:  {bed_type.get()}\nRoom Type:  {room_type.get()}\n=====================================\nCheck-In Date:   {check_in_date}\nCheck-Out Date:  {t}\nNumber of Days:  {days}\n=====================================\nAmount Paid:  {depo} Rs\n=====================================\nBill Time:  {time_and_date}\n Thank You\n=====================================\n")

        qr_code = qrcode.make(qr_data)
        qr_code = resizeimage.resize_cover(qr_code,[400,400])

        qr_code.save(f"Customer_QR/"+str(name)+".png")

        global im
        im = ImageTk.PhotoImage(file="Customer_QR/"+str(name)+'.png')
        qr_code_1.config(image=im)

        pdf = FPDF()

        pdf.add_page()
        pdf.set_left_margin(40)
        pdf.set_font("Arial" ,size = 16)

        with open(f"Customer_PDF/{combo_1.get()}.txt" , "w") as f:
            a = f.write(qr_data)

        file = open(f"Customer_PDF/{combo_1.get()}.txt","r")

        for i in file:
            pdf.cell(130,15,txt = i , ln = 1 ,align = "C")

        pdf.output(f"Customer_PDF/{combo_1.get()}.pdf")

    else:
        messagebox.showerror("Error" , "Pending Amount Remaining")

#--------------------------------------------------------------------------------------------- 

def pdf_mail():

    pen = pending_amount.get()

    if(int(pen) == 0):
        gmail()

    else:
         messagebox.showerror("Error" , "Pending Amount Remaining")

#---------------------------------------------------------------------------------------------

def mail_send():

    sendermail="hotelsunshine07@gmail.com"
    receivermail = f"{email.get()}"
    senderpass = "sunshine@07"
    subject = "Hotel Sunshine Invoice"
    bodyofmail = "Copy of your Invoice is attached below: "
    filename = f"{combo_1.get()}"
    location = "V:\Hotel Management System\HMS_PYTHON\Customer_PDF/"

    send = sendpdf(sendermail,receivermail,senderpass,subject,bodyofmail,
    filename,location)

    send.email_send()
    messagebox.showinfo("Succees" , "Email Send Successfully")

    root.destroy()

#---------------------------------------------------------------------------------------------

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

            day = row[10]  
            depo = row[7]  

        cursor_1 = connect_.cursor()
        cursor_1.execute("select * from room where room_number = '" +room_number.get()+ "'")
        res1 = cursor_1.fetchall()

        for r in res1:
            bed_type.set(r[4])
            room_type.set(r[5])

            price = r[3]

        pending = (int(day) * int(price)) - int(depo)

        pending_amount.set(pending)

        connect_.commit()
        connect_.close()

        s = pending_amount.get()
        
    except Exception as e:

        # messagebox.showerror("Error" , e)
        messagebox.showerror("Error" , "Please Select Customer Name")

#--------------------------------------------------------------------------------------------- 

def check_out():
    
    name = combo_1.get()

    s = pending_amount.get()

    if(int(s) == 0):

        date_ = t

        try:

            connect_ = pymysql.connect(host = "localhost" , user = "root" ,
            password = "123456789" ,database = "hotel")

            cursor_ = connect_.cursor()
            cursor_.execute(f"update customer set status = 'Out' where name = '"+name+"'")
            cursor_.execute(f"update room set available = 'Available' where room_number = '"+room_number.get()+"'")
            cursor_.execute(f"update room set status = 'Dirty' where room_number = '"+room_number.get()+"'")
            cursor_.execute(f"update customer set check_out_date = '"+date_+"' where name = '"+name+"'")

            messagebox.showinfo("Succees" , "Check Out Done Successfully")
 
            connect_.commit()
            connect_.close()

        except Exception as e:
            messagebox.showerror("Error",f"{e}")
    else:
        messagebox.showerror("Error" , "Pending Amount Remaining")

#---------------------------------------------------------------------------------------------

root.configure(bg = "white")
root.title("Check Out")
root.minsize(1250,680)
root.maxsize(1250,680)
root.geometry("1250x680+70+53")

l2 = Label(root,text="Check-Out Details" ,font = f"Tahoma 30" ,fg ="blue",
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
    check_in_date = i[8]
    days = i[10]

global combo_1

combo_1 = ttk.Combobox(root, values = l,  font = "Tahoma 16",justify = CENTER,
background="white",foreground="black",width=22,state="readonly")

combo_1.set("Search")
combo_1.place(x = 330,y = 78)

name = combo_1

l3 = Label(root,text="Customer Id" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=35,y=140)

id = StringVar()

t1 = Entry(root , textvariable = id , font = "Tahoma 17",state="readonly",justify = CENTER,
border = 2).place(x = 330 , y = 140)

l4 = Label(root,text="Id Number" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=35,y=205)

number = StringVar()

t2 = Entry(root , textvariable = number , font = "Tahoma 17",state="readonly",justify = CENTER,
border = 2).place(x = 330 , y = 205)

l5 = Label(root,text="Room Number" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=35,y=265)

room_number = StringVar()

t3 = Entry(root , textvariable = room_number , font = "Tahoma 17",state="readonly",justify = CENTER,
border = 2).place(x = 330 , y = 265)

l6 = Label(root,text="Bed Type" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=35,y=330)

bed_type = StringVar()

t4 = Entry(root , textvariable = bed_type, font = "Tahoma 17",state="readonly",justify = CENTER,
border = 2).place(x = 330 , y = 330)

l7 = Label(root,text="Room Type" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=35,y = 400)

room_type = StringVar()

t5 = Entry(root , textvariable = room_type, font = "Tahoma 17",justify = CENTER,state="readonly",
border = 2).place(x = 330 , y = 400)

l8 = Label(root,text="Check Out Date" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=35,y=470)

t = time.strftime('%Y / %m / %d',time.localtime())
time_and_date = time.strftime('%Y / %m / %d %H:%M:%S',time.localtime())

time_ = StringVar(value = t)

t6 = Entry(root , font = "Tahoma 17", textvariable = time_ ,state="readonly",justify = CENTER,
border = 2).place(x = 330 , y = 470)


l9 = Label(root,text="Pending Amount" ,font = "Tahoma 20" ,fg ="black",
bg ="white").place(x=35,y=540)

pending_amount = StringVar()

t7 = Entry(root , textvariable = pending_amount, font = "Tahoma 17",state="readonly",justify = CENTER,
border = 2).place(x = 330 , y = 540)

b1 = Button(root,bg = "black" , fg = "white" ,text = "Check" ,
font="Tahoma 17",border = 2, padx=70,cursor = "hand2",width = 3 , command=check).place(x=30,y=620)

b2 = Button(root,bg = "black" , fg = "white" ,text = "Check-Out" ,
font="Tahoma 17",border = 2, padx=70,cursor = "hand2",width = 3 , command=check_out).place(x=240,y=620)

b3 = Button(root,bg = "black" , fg = "white" ,text = "Back" ,
font="Tahoma 17",border = 2, padx=75,cursor = "hand2",width = 3 , command=back).place(x=450,y=620)

#--------------------------------------------------------------------------------------------- 

qr_frame=Frame (root,relief=RIDGE,bg='white' , bd = 2)
qr_frame.place(x=680,y=100,width=520,height=570)
        
la=Label(qr_frame,text='QR Code',font=("Thaoma",25),bg='#043256',fg='white',justify=CENTER)
la.place(x=0,y=0,width=520,height=70)

qr_code_1=Label(qr_frame,text='No QR\nAvailable',font=("Thaoma",25),bg='#3f51b5',
bd=1,relief=RIDGE,justify=CENTER,)

qr_code_1.place(x=70,y=80,width=400,height=400)
        
b4=Button(qr_frame,text="Generate QR",font=("Thaoma",18),fg='white',bg='black',bd=3,
cursor='hand2',command = qr)

b4.place(x=185,y=500,width=180,height=50)

img = Image.open("V:\\Hotel Management System\\icons\\gmail.png")
resized = img.resize((100,80), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(resized)

b5 = Button(root,image=photo,borderwidth=0,cursor = "hand2",
relief=RIDGE,command=pdf_mail).place(x = 1100 , y = 8)

#---------------------------------------------------------------------------------------------     

def gmail():

    mail_frame=Frame(bd=2,relief=RIDGE,bg='white')
    mail_frame.place(x=400,y=250,width=600,height=140)

    l_mail = Label(mail_frame,text="Email Address" ,font = "Tahoma 20" ,fg ="black",
    bg ="white").place(x=20,y=20)

    global email

    email = StringVar()

    t_mail = Entry(mail_frame , textvariable = email , font = "Tahoma 17",
    border = 2).place(x = 210 , y = 23,width=380)

    b_1_mail = Button(mail_frame,bg = "black" , fg = "white" ,text = "Send" ,
    font="Tahoma 15",border = 2, padx=30,cursor = "hand2",width = 9
    ,command = mail_send).place(x=130,y=80)

    b_2_mail = Button(mail_frame,bg = "black" , fg = "white" ,text = "Close" ,
    font="Tahoma 15",border = 2, padx=30,cursor = "hand2",width = 9
    ,command=root.destroy).place(x=340,y=80)


root.mainloop()
