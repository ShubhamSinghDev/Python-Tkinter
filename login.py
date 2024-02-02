import tkinter as tk
import pymysql
from tkinter import messagebox
from PIL import ImageTk, Image

frame=tk.Tk()
frame.geometry("500x450")
img = ImageTk.PhotoImage(file='photos.png')
frame.iconphoto(False, img)

frame.title("Login Form")

frame.resizable(False,False)
frame.configure(bg="#333333")
def log():
    
    Email=E1.get()
    pss=E2.get()
    
    con=pymysql.connect(host="localhost",user="root",password="",db="shubham",port=3307)
    cur=con.cursor()
    
    q1="select * from `register` where `Email`='"+Email+"' and `Password`='"+pss+"'"
    cur.execute(q1)
    #data=cur.fetchall()
    #print(data)
    count=0
    for x in cur:
        count+=1
        print("s")
    
    if count==1:
        print("Login")
        frame.destroy()
        import multi_frame_in_one
    else:
        print("Invalid Login")
        
def reg():
    frame.destroy()
    import Registration


top=tk.Label(frame, text="Login", font=("Segoe UI Variable", 45),bg="#333333",fg="#FFFFFF")
top.place(x=170,relx=0,rely=0.05,relwidth=0.3,relheight=0.15)

L1=tk.Label(frame,text="Email",font=("Arail",22),bg="#333333",fg="#FFFFFF")
L1.place(relx=0,rely=0.27,relwidth=0.45,relheight=0.15)

E1=tk.Entry(frame,text="",font=("Arial",22))
E1.place(relx=0.46,rely=0.27,relwidth=0.45,relheight=0.15)

L2=tk.Label(frame,text="Password",font=("Arial",22),bg="#333333",fg="#FFFFFF")
L2.place(relx=0,rely=0.49,relwidth=0.45,relheight=0.15)

E2=tk.Entry(frame,text="",font=("Arial",22))
E2.place(relx=0.46,rely=0.49,relwidth=0.45,relheight=0.15)

B1=tk.Button(frame,text="Login",font=("Arial",20),command=log,bg="#FF3399",fg="#FFFFFF",border=10)
B1.place(relx=0.15,rely=0.7,relwidth=0.3,relheight=0.15)

B2=tk.Button(frame,text="Reg",font=("Arial",20),command=reg,bg="#FF3399",fg="#FFFFFF",border=10)
B2.place(relx=0.55,rely=0.7,relwidth=0.3,relheight=0.15)
frame.mainloop()
