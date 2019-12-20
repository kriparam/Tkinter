from tkinter import *
win =Tk();
win.geometry("400x250")
label=Label(win,text="List Of Students")
listbox=Listbox(win)
listbox.insert(1,"ram")
listbox.insert(2,"shyam")
listbox.insert(3,"sheeta")
listbox.insert(4,"geeta")
listbox.insert(5,"mohan")
listbox.insert(6,"radhika")
listbox.insert(7,"krishna")
button=Button(win,text="delete" , command=lambda listbox=listbox:listbox.delete(ANCHOR))
label.pack()
listbox.pack()
button.pack()
win.mainloop();