from tkinter import *
def call_result(label_result,n1,n2):
    num1=(n1.get())
    num2=(n2.get())
    result=int(num1)+int(num2)
    label_result.config(text="result=%d"% result)
    return
win =Tk();
win.geometry("400x250")
win.title("calculator")
num1=Label(win,text="First number").grid(row=1,column="0")
num2=Label(win,text="Second number").grid(row=2,column="0")
label_result=tk.Label(win)
label_result.grid(row=7,column=2)
e1=Entry(win).grid(row=1,column=2)
e2=Entry(win).grid(row=2,column=2)
button=Button(win,text="Calculate", command="call_result").grid(row=3,column="0")
win.mainloop();