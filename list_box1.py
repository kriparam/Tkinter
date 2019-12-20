from tkinter import *
win =Tk();
win.geometry("400x250")
label=Label(win,text="list of Programming languages")
listbox=Listbox(win)
listbox.insert(1,"C")
listbox.insert(2,"C++")
listbox.insert(3,"Java")
listbox.insert(4,"python")
label.pack()
listbox.pack()
win.mainloop();