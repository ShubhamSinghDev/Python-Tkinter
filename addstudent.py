import tkinter as tk
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
def submit(E1,E2,E3,E4,E5,E6):
    global frame
    global var1
    global var2
    global var3
    global var4
    t1=E1.get().strip()
    t2=E2.get().strip()
    t3=E3.get().strip()
    t4=var3.get()#gender
    t5=var2.get()#nationality
    #t6=E6.get().strip()
    if(t1=="" or t2=="" or t3==""):
        var4.set("Please filled properly")
    else:
        var4.set("Everything alright")
        try:
            conn=pymysql.connect(host="localhost",user="root",password="",db="sas",port=3307)
            cur=conn.cursor()
            q2="select * from student where `email`='"+t2+"'"
            e2=cur.execute(q2)
            count=0
            for x in cur:
                count+=1
            if(count==0):
                q3="INSERT INTO `student`(`name`, `email`, `nationality`, `gender`, `password`, `status`) VALUES ('"+t1+"','"+t2+"','"+t5+"','"+t4+"','"+t3+"','1')"
                e3=cur.execute(q3)
                conn.commit()
                var4.set("inserted")
                
            else:
                frame.destroy()
                var4.set("Email Already Exist")
        except:
            var4.set("please check connection")
    print(s1)
    pass
    

def disp(m1):
    global frame
    global var1
    global var2
    global var3
    global var4
    frame=tk.Tk()
    frame.geometry("1500x800")
    frame.title("Add Student")

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

    options = [ 
    "India", 
    "Srilanka", 
    "Bangladesh"
    ]
    var2=tk.StringVar()
    var2.set("Select an Option")
    
    L3=tk.Label(frame2,text="Name",font=("Arial", 18))
    L3.place(relx=0,rely=0,relwidth=0.49,relheight=0.1)
    E1=tk.Entry(frame2,text="",font=("Arial", 18),bd=5)
    E1.place(relx=0.5,rely=0,relwidth=0.49,relheight=0.1)

    L4=tk.Label(frame2,text="Email",font=("Arial", 18))
    L4.place(relx=0,rely=0.12,relwidth=0.49,relheight=0.1)
    E2=tk.Entry(frame2,text="",font=("Arial", 18),bd=5)
    E2.place(relx=0.5,rely=0.12,relwidth=0.49,relheight=0.1)

    L5=tk.Label(frame2,text="Password",font=("Arial", 18))
    L5.place(relx=0,rely=0.24,relwidth=0.49,relheight=0.1)
    E3=tk.Entry(frame2,text="",show="*",font=("Arial", 18),bd=5)
    E3.place(relx=0.5,rely=0.24,relwidth=0.49,relheight=0.1)

    L6=tk.Label(frame2,text="Gender",font=("Arial", 18))
    L6.place(relx=0,rely=0.36,relwidth=0.49,relheight=0.1)
    E4=tk.Radiobutton(frame2,text="M",variable=var3,value="M",font=("Arial", 18),bd=5)
    E4.place(relx=0.5,rely=0.36,relwidth=0.1,relheight=0.1)
    E5=tk.Radiobutton(frame2,text="F",variable=var3,value="F",font=("Arial", 18),bd=5)
    E5.place(relx=0.65,rely=0.36,relwidth=0.1,relheight=0.1)

    L7=tk.Label(frame2,text="Nationality",font=("Arial", 18))
    L7.place(relx=0,rely=0.48,relwidth=0.49,relheight=0.1)
    E6=tk.OptionMenu(frame2, var2, *options)
    E6.place(relx=0.5,rely=0.48,relwidth=0.4,relheight=0.1)

    B2=tk.Button(frame2,text="Submit",font=("Arial", 18),bd=5,command=lambda:submit(E1,E2,E3,E4,E5,E6))
    B2.place(relx=0.4,rely=0.6,relwidth=0.2,relheight=0.1)

    L8=tk.Label(frame2,text="",textvariable=var4,font=("Arial", 18))
    L8.place(relx=0.2,rely=0.8,relwidth=0.6,relheight=0.1)
    
    B3=tk.Button(frame,text="All Student",font=("Arial", 18),bd=5,command=allstudent)
    B3.place(relx=0.4,rely=0.8,relwidth=0.2,relheight=0.1)
    
    frame.mainloop()
disp("aict")
