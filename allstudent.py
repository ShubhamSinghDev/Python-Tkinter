import tkinter as tk
from tkinter import ttk
import pymysql



def logout():
    frame.destroy()
    import home
def addstudent():
    frame.destroy()
    import addstudent
    addstudent.disp(var1.get())
def allstudent():
    frame.destroy()
    import allstudent
    allstudent.disp(var1.get())
    

def disp(m1):
    global frame
    global var1
    global var2
    global var3
    global var4
    
    frame=tk.Tk()
    frame.geometry("1500x800")
    frame.title("All Student")

    var1=tk.StringVar()
    var2=tk.StringVar()
    var3=tk.StringVar()
    var4=tk.StringVar()
    var1.set(m1)
    L1=tk.Label(frame,text="Welcome",font=("Arial", 18))
    L1.place(relx=0,rely=0,relwidth=0.1,relheight=0.1)
    L2=tk.Label(frame,text="name",textvariable=var1,font=("Arial", 18))
    L2.place(relx=0.12,rely=0,relwidth=0.1,relheight=0.1)

    B1=tk.Button(frame,text="Logout",font=("Arial", 18),bd=5,command=logout)
    B1.place(relx=0.89,rely=0.0,relwidth=0.1,relheight=0.1)

    frame2=tk.Frame(frame,bg="#00ffff")
    frame2.place(relx=0.1,rely=0.12,relwidth=0.8,relheight=0.67)
    # define columns
    columns = ('name', 'email', 'nationality','gender','status')
    tree = ttk.Treeview(frame2, columns=columns, show='headings')
    # define headings
    tree.heading('name', text='Name')
    tree.heading('email', text='Email')
    tree.heading('nationality', text='Nationality')
    tree.heading('gender', text='gender')
    tree.heading('status', text='status')
    tree.place(relx=0,rely=0,relwidth=1,relheight=1)
    try:
        conn=pymysql.connect(host="localhost",user="root",password="",db="aict",port=3307)
        cur=conn.cursor()
        q2="select `name`,`email`,`nationality`,`gender`,`status` from `student`"
        e2=cur.execute(q2)
        count=0
        for x in cur:
            print(x)
            tree.insert('', tk.END, values=x)
            count+=1
        if(count==0):
            var1.set("No Record Found")
            
    except:
        var1.set("please check connection")
    scrollbar = ttk.Scrollbar(frame2, orient = "vertical", command = tree.yview)  
    scrollbar.place(relx=1, rely=0, relheight=1, anchor='ne') 
    tree.configure(xscrollcommand = scrollbar.set)
    
    B3=tk.Button(frame,text="Add Student",font=("Arial", 18),bd=5,command=addstudent)
    B3.place(relx=0.4,rely=0.8,relwidth=0.2,relheight=0.1)
    
    frame.mainloop()
disp("aict")
