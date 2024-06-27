#Task : Use the logical operator to combine the is else coditions under the check functions. You can use chatgpt.

import tkinter as tk
from tkinter import messagebox

def check():



def add():
    check()
    n1=int(number1.get())
    n2=int(number2.get())
    answer.config(text=n1+n2)

def subtract():
    check() #call the function check
    n1=int(number1.get())
    n2=int(number2.get())
    answer.config(text=n1-n2)

def multiply():
    check() #call the function check
    n1=int(number1.get())
    n2=int(number2.get())
    answer.config(text=n1*n2)

def divide():
    check() #call the function check
    n1=int(number1.get())
    n2=int(number2.get())
    answer.config(text=n1/n2)

window=tk.Tk()
window.title("Calculator Application")
window.geometry("400x300")
text=tk.Label(window,text="Calculator")
text.pack()

number1=tk.Entry(window)
number1.pack(padx=5,pady=5)

number2=tk.Entry(window)
number2.pack(padx=5,pady=5)
frame=tk.Frame(window)
frame.pack(padx=20,pady=20)

button1=tk.Button(frame,text="+",command=add)
button1.grid(row=0,column=1,padx=5,pady=5)
button2=tk.Button(frame,text="-",command=subtract)
button2.grid(row=0,column=2,padx=5,pady=5)
button3=tk.Button(frame,text="*",command=multiply)
button3.grid(row=0,column=3,padx=5,pady=5)
button4=tk.Button(frame,text="/",command=divide)
button4.grid(row=0,column=4,padx=5,pady=5)

answer=tk.Label(window,text="Answer")
answer.pack()
window.mainloop()
