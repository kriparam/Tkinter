from tkinter import *
win =Tk();
win.geometry("400x250")
frame=Frame(win).pack()
rightframe=Frame(win).pack()
button=Button(frame,text="button1").pack()
button1=Button(rightframe,text="button2").pack()
win.mainloop();