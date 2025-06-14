import tkinter as tk
import pymysql
import profile

def login():
    t1=E1.get().strip()
    t2=E2.get().strip()
    if(t1==""):
        var1.set("Please Enter Adminid")
    elif(t2==""):
        var1.set("Please Enter Password")
    else:
        var1.set("Everything alright")
        try:
            conn=pymysql.connect(host="localhost",user="root",password="",db="sas",port=3307)
            cur=conn.cursor()
            q2="select * from admin where `adminid`='"+t1+"' and `password`='"+t2+"'"
            e2=cur.execute(q2)
            count=0
            for x in cur:
                count+=1
            if(count==0):
                var1.set("invalid login details")
            else:
                frame.destroy()
                profile.disp(t1)
                var1.set("valid login details")
        except:
            var1.set("please check connection")


frame=tk.Tk()
frame.geometry("400x400")
frame.title("Admin Login")

L1=tk.Label(frame,text="AdminId",font=("Arial", 18))
L1.place(relx=0,rely=0,relwidth=0.49,relheight=0.1)
E1=tk.Entry(frame,text="",font=("Arial", 18),bd=5)
E1.place(relx=0.5,rely=0,relwidth=0.49,relheight=0.1)

L2=tk.Label(frame,text="Password",font=("Arial", 18))
L2.place(relx=0,rely=0.11,relwidth=0.49,relheight=0.1)
E2=tk.Entry(frame,text="",show="*",font=("Arial", 18),bd=5)
E2.place(relx=0.5,rely=0.11,relwidth=0.49,relheight=0.1)

B1=tk.Button(frame,text="Login",font=("Arial", 18),bd=5,command=login)
B1.place(relx=0.3,rely=0.22,relwidth=0.4,relheight=0.1)

var1=tk.StringVar()

L3=tk.Label(frame,text="invalid login details",textvariable=var1,font=("Arial", 18),fg="red")
L3.place(relx=0.1,rely=0.40,relwidth=0.8,relheight=0.1)
frame.mainloop()
