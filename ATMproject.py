from tkinter import *
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",passwd="gos123",database="bank")
if con.is_connected():
    print("succesfully connected to my sql")
def func():
    sql="select acc_number,pin from atm where acc_number={} and pin={} ;".format(ent.get(),password.get())
    global acc_num
    acc_num=ent.get()
    cursor.execute(sql)
    result=cursor.fetchall()
    con.commit()
    acc_num=int(ent.get())
    pin=int(password.get())
    for i in result:
        if acc_num == i[0] and i[1] == pin:
            fun()          
        else:
            print("invalid")
               
win=Tk()
win.title("ATM")
win.configure(background="grey")
win.minsize(width=500,height=400)
win.maxsize(width=500,height=400)
cursor=con.cursor()
lbl= Label(win,text="PLEASE ENTER ACCOUNT NUMBER",bg="blue",fg="white",width=30,height=3,font=("bold", 10))
lbl.place(x=10,y=130)
lol=IntVar()
ent=Entry(win,textvariable=lol)
ent.place(x=270,y=145)
lbl= Label(win,text="PIN",bg="blue",fg="white",width=30,height=3,font=("bold",10))
lbl.place(x=10,y=200)
password=Entry(win)
password.place(x=270,y=215)
btn=Button(win,text="ENTER",bg="blue",fg="white",command=func,font=("bold",10))
btn.place(x=430,y=24)
sql="select acc_number,pin from atm where acc_number={} and pin={} ;".format(ent.get(),password.get())

#-------------------------------------------------------------button modules------------------------------------------------------------------------------------------------------------------
   
def fun():
    win=Tk()
    win.configure(background="grey")
    win.title("ATM")
    win.minsize(width=750,height=370)
    win.maxsize(width=750,height=370)

    #withdraw statement
    lbl= Label(win,text="CASH WITHDRAWAL",bg="blue",fg="white",width=17,height=4,font=("bold", 10))
    lbl.place(x=143,y=10)
    btn=Button(win,text=">>>>",width=15,height=3,bg="blue",fg="white",font=("bold",10),command=withdraw)
    btn.place(x=10,y=10)

    #pin change
    lbl= Label(win,text="PIN CHANGE",bg="blue",fg="white",width=17,height=4,font=("bold", 10))
    lbl.place(x=143,y=290)
    btn=Button(win,text=">>>>",width=15,height=3,bg="blue",fg="white",font=("bold",10),command=change_pin)
    btn.place(x=10,y=290)
   
    #create new account
    lbl= Label(win,text="NEW ACCOUNT",bg="blue",fg="white",width=15,height=4,font=("bold", 10))
    lbl.place(x=467,y=10)
    btn=Button(win,text="<<<<",width=15,height=3,bg="blue",fg="white",font=("bold",10),command=add_acc)
    btn.place(x=600,y=10)

    #cash deposit
    lbl=Label(win,text="CASH DEPOSIT",width=15,height=4,bg="blue",fg="white",font=("bold",10))
    lbl.place(x=467,y=150)
    btn=Button(win,text="<<<<",width=15,height=3,bg="blue",fg="white",font=("bold",10),command=withdrawal)
    btn.place(x=600,y=150)



      #transaction history
    lbl=Label(win,text="TRANSACTION HISTORY",width=20,height=4,bg="blue",fg="white",font=("bold",10))
    lbl.place(x=430,y=290)
    btn=Button(win,text="<<<<",width=15,height=3,bg="blue",fg="white",font=("bold",10),command=records)
    btn.place(x=600,y=290)



    #balance enquiry
    lbl= Label(win,text="BALANCE ENQUIRY",bg="blue",fg="white",width=17,height=4,font=("bold", 10))
    lbl.place(x=143,y=150)
    btn=Button(win,text=">>>>",width=15,height=3,bg="blue",fg="white",font=("bold",10),command=enquire)
    btn.place(x=10,y=150)

#----------------------------------------------------------------balance enquiry--------------------------------------------------------------------------------------------

LAN=mysql.connector.connect(host="localhost",user="root",passwd="gos123",database="bank")

def enquire():
    print(acc_num)
    print(type(acc_num))

    def BE():

        cursor=con.cursor()
        sql="select acc_number,balance from atm where acc_number={};".format(acc_num)
        cursor.execute(sql)
        result=cursor.fetchall()
        cursor=con.commit()
        accc=int(ent.get())
        print(result)
        for i in result:
            print(accc)
            print(type(accc))
            if i[0] == accc :
             amt=i[1]
             bo= Label(win,text="your balance is:",bg="blue",fg="white",width=30,height=3,font=("bold", 10))
             bo.place(x=100,y=100)
             sike= Label(win,text=amt,bg="blue",fg="white",font=("bold", 13))
             sike.place(x=280,y=115)
            else:
                continue

    win=Tk()
    win.configure(background="grey")
    win.title("ATM")
    win.minsize(width=700,height=600)
    win.maxsize(width=700,height=600)  
    lbl= Label(win,text="PLEASE ENTER ACCOUNT NUMBER",bg="blue",fg="white",width=30,height=3,font=("bold", 10))
    lbl.place(x=10,y=10)
    ent=Entry(win)
    ent.place(x=270,y=25)
    btn=Button(win,text="ENTER",bg="blue",fg="white",command=BE,font=("bold",10))
    btn.place(x=450,y=55)
    btn=Button(win,text="BACK",bg="blue",fg="white",command=BE,font=("bold",10))
    btn.place(x=300,y=55)    
    win.mainloop()                
           
#------------------------------------------------add new account----------------------------------------------------------------------------------------------------------------------


conn=mysql.connector.connect(host="localhost",user="root",passwd="gos123",database="bank")
def add_acc():

    def funt():
        cursor=conn.cursor()
        acc_nu=ent.get()
        pin=bla.get()
        name_=name.get()
        phone_number=phone.get()
        acc_nume=int(acc_nu)
        pin=int(pin)
        phone_number=int(phone_number)
        balance="null"
        sql="insert into atm values({},{},'{}',{},{});".format(acc_num,pin,name_,phone_number,balance)
        cursor.execute(sql)
        con.commit()
       #display
        lbl= Label(win,text="NEW ACCOUNT CREATED",bg="blue",fg="white",width=40,height=3,font=("bold", 10))
        lbl.place(x=270,y=270)
   
    #window      
    win=Tk()
    win.configure(background="grey")
    win.title("ATM")
    win.minsize(width=700,height=600)
    win.maxsize(width=700,height=600)


      #entry input of account number
    ent=Entry(win)
    ent.place(x=350,y=20)
  #entry input of pin
    bla=Entry(win)
    bla.place(x=350,y=60)
 #entry input of name
    name=Entry(win)
    name.place(x=350,y=120)
 #entry input of phone number
    phone=Entry(win)
    phone.place(x=350,y=170)

     #display
    lbl= Label(win,text="PLEASE ENTER ACCOUNT NUMBER",bg="blue",fg="white",width=40,height=3,font=("bold", 10))
    lbl.place(x=10,y=10)
    #display
    lbl= Label(win,text="PLEASE ENTER PIN TO SET",bg="blue",fg="white",width=40,height=3,font=("bold", 10))
    lbl.place(x=10,y=50)
     #display
    lbl= Label(win,text="PLEASE ENTER NAME TO SET",bg="blue",fg="white",width=40,height=3,font=("bold", 10))
    lbl.place(x=10,y=100)
     #display
    lbl= Label(win,text="PLEASE ENTER PHONE NUMBER TO SET",bg="blue",fg="white",width=40,height=3,font=("bold", 10))
    lbl.place(x=10,y=150)


#button to accept
    btn=Button(win,text="ENTER",bg="blue",fg="white",command=funt,font=("bold",10))
    btn.place(x=270,y=235)

    #button to accept
    btn=Button(win,text="BACK",bg="blue",fg="white",command=fun,font=("bold",10))
    btn.place(x=10,y=235)

#---------------------------------------------------------------------------cash withdrawal----------------------------------------------------------------------------------------------          

con1=mysql.connector.connect(host="localhost",user="root",passwd="gos123",database="bank")
def withdraw():
    def acc():
        acc_number=ent.get()
        acc_number=int(acc_num)
        sql="select acc_number,balance from atm where acc_number={}".format(acc_number)
        cursor=con1.cursor()
        cursor.execute(sql)
        balance=cursor.fetchall()
        con.commit()
        amt=hah.get()
        amt=int(amt)
        acc=int(ent.get())
        for row in balance:
            if row[0] == acc:
                    if row[1] >= amt:
                        S="update atm set balance = balance-{} where acc_number={};".format(amt,acc_number)
                        cursor=con.cursor()
                        cursor.execute(S)
                        con.commit()
                        lo=Label(win,text="AMOUNT SUCCESFULLY WITHDRAWN",bg="blue",fg="white",width=40,height=3,font=("bold", 10))
                        lo.place(x=270,y=170)
                        Cursor=MAN.cursor()
                        SQL="insert into TRANS(acc_num,bal,amt_with,cas_depo,cur_dat) values({},{},{},{},curdate())".format(acc_number,row[0],amt,0)
                        Cursor.execute(SQL)
                        MAN.commit()
                    else:
                        lo=Label(win,text="INSUFFICIENT FUNDS",bg="blue",fg="white",width=40,height=3,font=("bold", 10))
                        lo.place(x=270,y=170)
             
    #window      
    win=Tk()
    win.configure(background="grey")
    win.title("ATM")
    win.minsize(width=700,height=600)
    win.maxsize(width=700,height=600)

    #entry input of account number
    lol=IntVar()
    ent=Entry(win,textvariable=lol)
    ent.place(x=270,y=20)

    #display
    lbl= Label(win,text="PLEASE ENTER ACCOUNT NUMBER",bg="blue",fg="white",width=30,height=3,font=("bold", 10))
    lbl.place(x=10,y=10)

    #entry input of amount
    lol=IntVar()
    hah=Entry(win,textvariable=lol)
    hah.place(x=270,y=90)

    #display off amt
    lbl= Label(win,text="ENTER AMT TO WITHDRAW",bg="blue",fg="white",width=30,height=3,font=("bold", 10))
    lbl.place(x=10,y=70)

    #button to accept
    btn=Button(win,text="ENTER",bg="blue",fg="white",command=acc,font=("bold",10))
    btn.place(x=270,y=150)

     #button to go back
    btn=Button(win,text="BACK",bg="blue",fg="white",command=fun,font=("bold",10))
    btn.place(x=10,y=150)

#---------------------------------------------------------------------------------------cash deposit-------------------------------------------------------------------------------------            

con2=mysql.connector.connect(host="localhost",user="root",passwd="gos123",database="bank")
def withdrawal():
   
   
    def acc():
        acc_number=ent.get()
        acc_number=int(acc_number)
        sql="select acc_number,balance from atm where acc_number={}".format(acc_num)
        cursor=con2.cursor()
        cursor.execute(sql)
        balance=cursor.fetchall()
        con.commit()
        amt=hah.get()
        amt=int(amt)
        for row in balance:
            if row[0] == acc_number:
                S="update atm set balance = balance+{} where acc_number={};".format(amt,acc_number)
                cursor=con.cursor()
                cursor.execute(S)
                con.commit()
                lo=Label(win,text="AMOUNT SUCCESFULLY DEPOSITED",bg="blue",fg="white",width=40,height=3,font=("bold", 10))
                lo.place(x=270,y=190)
                Cursor=MAN.cursor()
                SQL="insert into TRANS(acc_num,bal,amt_with,cas_depo,cur_dat) values({},{},{},{},curdate())".format(acc_number,row[0],0,amt)
                Cursor.execute(SQL)
                MAN.commit()
    #window      
    win=Tk()
    win.configure(background="grey")
    win.title("ATM")
    win.minsize(width=700,height=600)
    win.maxsize(width=700,height=600)

    #entry input of account number
    lol=IntVar()
    ent=Entry(win,textvariable=lol)
    ent.place(x=270,y=20)

    #display
    lbl= Label(win,text="PLEASE ENTER ACCOUNT NUMBER",bg="blue",fg="white",width=30,height=3,font=("bold", 10))
    lbl.place(x=10,y=10)

    #entry input of amount
    lol=IntVar()
    hah=Entry(win,textvariable=lol)
    hah.place(x=270,y=90)


    #display off amt
    lbl= Label(win,text="ENTER AMT TO DEPOSIT",bg="blue",fg="white",width=30,height=3,font=("bold", 10))
    lbl.place(x=10,y=70)


    #button to accept
    btn=Button(win,text="ENTER",bg="blue",fg="white",command=acc,font=("bold",10))
    btn.place(x=270,y=150)

     #button to go back
    btn=Button(win,text="BACK",bg="blue",fg="white",command=fun,font=("bold",10))
    btn.place(x=10,y=150)

#----------------------------------------------------------------------------------------pin change----------------------------------------------------------------------


con3=mysql.connector.connect(host="localhost",user="root",passwd="gos123",database="bank")
def change_pin():

   
    def fun():
        acc_numbe=ent.get()
        oldpin=bla.get()
        new_pin=name.get()
        sql="select acc_number,pin from atm where acc_number={};".format(acc_num)
        cursor=con3.cursor()
        cursor.execute(sql)
        result=cursor.fetchall()
        con.commit()
        acc_numbe=int(acc_numbe)
        oldpin=int(oldpin)
        new_pin=int(new_pin)
        for i in result:
            if i[0]== acc_numbe:
                if i[1] == oldpin:
                    sql1="update atm set pin={} where acc_number={};".format(new_pin,acc_numbe)
                    cursor1=con.cursor()
                    cursor1.execute(sql1)
                    con.commit()
                 #display
                    lbl= Label(win,text="PIN SUCCESFULLY CHANGED",bg="blue",fg="white",width=40,height=3,font=("bold", 10))
                    lbl.place(x=270,y=270)
                else:
                #display
                    lbl= Label(win,text="PIN INCORRECT",bg="blue",fg="white",width=40,height=3,font=("bold", 10))
                    lbl.place(x=270,y=270)       

   
    #window      
    win=Tk()
    win.configure(background="grey")
    win.title("ATM")
    win.minsize(width=700,height=600)
    win.maxsize(width=700,height=600)
    #display
    lbl= Label(win,text="PLEASE ENTER ACCOUNT NUMBER",bg="blue",fg="white",width=40,height=3,font=("bold", 10))
    lbl.place(x=10,y=10)
     #display
    lbl= Label(win,text="PLEASE ENTER OLD PIN TO SET",bg="blue",fg="white",width=40,height=3,font=("bold", 10))
    lbl.place(x=10,y=50)
     #display
    lbl= Label(win,text="PLEASE ENTER NEW PIN TO SET",bg="blue",fg="white",width=40,height=3,font=("bold", 10))
    lbl.place(x=10,y=100)

       #entry input of account number

    ent=Entry(win)
    ent.place(x=350,y=20)
      #entry input of old pin
    bla=Entry(win)
    bla.place(x=350,y=60)
     #entry input of new pin
    name=Entry(win)
    name.place(x=350,y=120)

    #button to accept
    btn=Button(win,text="ENTER",bg="blue",fg="white",command=fun,font=("bold",10))
    btn.place(x=270,y=235)


    #button to accept
    btn=Button(win,text="BACK",bg="blue",fg="white",command=fun,font=("bold",10))
    btn.place(x=10,y=235)

#-------------------------------------------------------transaction history-----------------------------------------------------------------------------------------------


from tkinter import ttk
from tkinter import CENTER

MAN=mysql.connector.connect(host="localhost",user="root",passwd="gos123",database="record")
con4=mysql.connector.connect(host="localhost",user="root",passwd="gos123",database="bank")
def records():
    def funcion():
        acc_numb=int(ent.get())
        pas=int(pin.get())
        cursor=MAN.cursor()
        cursor1=con4.cursor()
        sql="select acc_number,pin from atm where acc_number={}".format(acc_num)
        cursor1.execute(sql)
        result=cursor1.fetchall()
        con.commit()
        for i in result:
           
            if i[0] == acc_numb and i[1] == pas:
                SQL="select acc_num,bal,amt_with,cas_depo,cur_dat from TRANS where acc_num={}".format(acc_numb)
                cursor.execute(SQL)
                history = cursor.fetchall()
                r=Tk()
                r.title("transaction history")
                r.geometry("600x300")
                C=MAN.cursor()
                C.execute("select * from TRANS where acc_num={}".format(acc_num))
               
                tree=ttk.Treeview(r)
                tree["show"]="headings"

                tree["columns"]=("acc_num","bal","amt_with","cas_depo","cur_dat")
                tree.column("acc_num",width=50,minwidth=50,anchor=CENTER)
                tree.column("bal",width=50,minwidth=50,anchor=CENTER)
                tree.column("amt_with",width=50,minwidth=50,anchor=CENTER)
                tree.column("cas_depo",width=50,minwidth=50,anchor=CENTER)
                tree.column("cur_dat",width=50,minwidth=50,anchor=CENTER)

                tree.heading("acc_num",text="account number",anchor=CENTER)
                tree.heading("bal",text="balance",anchor=CENTER)
                tree.heading("amt_with",text="amount withdrawn",anchor=CENTER)
                tree.heading("cas_depo",text="amount deposited",anchor=CENTER)
                tree.heading("cur_dat",text="DATE",anchor=CENTER)

                i=0
                for z in C:
                    tree.insert('',i,values=(z[0],z[1],z[2],z[3],z[4]))
                    i=i+1
                tree.pack()

  #window
    win=Tk()
    win.configure(background="grey")
    win.title("ATM")
    win.minsize(width=500,height=500)
    win.maxsize(width=500,height=500)

  #entry input of account number
    lol=IntVar()
    ent=Entry(win,textvariable=lol)
    ent.place(x=270,y=20)


  #display
    lbl= Label(win,text="PLEASE ENTER ACCOUNT NUMBER",bg="blue",fg="white",width=30,height=3,font=("bold", 10))
    lbl.place(x=10,y=10)


  #entry of pin
    lol=IntVar()
    pin=Entry(win,textvariable=lol)
    pin.place(x=270,y=90)


    #display of pin entry
    lbl= Label(win,text="ENTER THE PIN",bg="blue",fg="white",width=30,height=3,font=("bold", 10))
    lbl.place(x=10,y=70)


 #button to accept
    btn=Button(win,text="ENTER",bg="blue",fg="white",command=funcion,font=("bold",10))
    btn.place(x=270,y=150)
     #button to go back
    btn=Button(win,text="BACK",bg="blue",fg="white",command=fun,font=("bold",10))
    btn.place(x=10,y=150)
