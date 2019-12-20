
from tkinter import *
win =Tk()
#variable=checkbutton(master, options)
checkvar=IntVar()
check1=checkbutton(win,text="check me",variable="checkvar")
check1.pack()
win.geometry("400x250")