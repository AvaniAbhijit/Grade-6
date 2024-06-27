#Task 1 : Run the code and keep text field 2 empty and try to do the addition. What happen when you keep 1 field empty?

import tkinter as tk
from tkinter import messagebox #importing messagebox module

def check(): #add a function to check if the field is empty
    if number1.get()=="": #using if condition to check if the first field is empty
        messagebox.showinfo("Error","Fields are empty") #if the field is empty, show an error message
    elif number2.get()=="": #using elif condition to check if the second field is empty
        messagebox.showinfo("Error","Fields are empty") #if the field is empty, show an error message.
    else: #if both fields are not empty
        return #return to the main function

def add():
    check() #calling the function check
    n1=int(number1.get())
    n2=int(number2.get())
    answer.config(text=n1+n2)

def subtract():
    n1=int(number1.get())
    n2=int(number2.get())
    answer.config(text=n1-n2)

def multiply():
    n1=int(number1.get())
    n2=int(number2.get())
    answer.config(text=n1*n2)

def divide():
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
