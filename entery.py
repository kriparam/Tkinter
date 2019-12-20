from tkinter import *
win =Tk();
win.title('Login Page')
win.geometry("400x250")
label=Label(win,text="welcome to login").place(x=70,y=10)
name=Label(win,text="Name").place(x=30,y=50)
email=Label(win,text="Email").place(x=30,y=90)
password=Label(win,text="pssword").place(x=30,y=130)
button=Button(win,text="Submit").place(x=30,y=170)
e1=Entry(win).place(x=80,y=50)
e2=Entry(win).place(x=80,y=90)
e3=Entry(win).place(x=80,y=130)
win.mainloop();