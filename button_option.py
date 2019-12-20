from tkinter import *
win =Tk()
win.geometry("400x250")
#def fun():
#messagebox.showinfo("hello","red button clicked")
#b1=Button(win,text="red"  , command=fun,activeforeground="green", padx=100)
b1=Button(win,text="red" ,activeforeground="white",activebackground="red", padx=20,highlightcolor="lightblue",relief="sunken").place(x=30,y=20)
b2=Button(win,text="blue" ,activeforeground="white",activebackground="blue", padx=20,relief="ridge")
b3=Button(win,text="green" ,activeforeground="white",activebackground="green", padx=20,fg="blue",relief="groove")
b4=Button(win,text="yellow" ,activeforeground="black",activebackground="yellow", padx=20,relief="raised",state="disabled")
#b1.pack(side=LEFT)

b2.pack(side=RIGHT)
b3.pack(side=TOP)

b4.pack(side=BOTTOM)







win.mainloop();