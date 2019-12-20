from tkinter import *
win =Tk();

def hello():
    print("hello!")
menubar = Menu(win)

menubar.add_command(label="Hello!", command=hello)
menubar.add_command(label="Quit!", command=win.quit)
win.config(menu=menubar)
win.mainloop();