#Task : Write the eval function code for division and multiplication button.

import tkinter as tk
from tkinter import messagebox

def check():
    if number1.get()=="":
        messagebox.showinfo("Error","Fields are empty")
    else:
        return

def calculate():
    answer.config(text=eval(number1.get()))

def add(text):
    number1.insert(tk.END,text)


window=tk.Tk()
window.title("Calculator Application")
window.geometry("400x300")
text=tk.Label(window,text="Calculator")
text.pack()

number1=tk.Entry(window)
number1.pack(padx=5,pady=5)

frame=tk.Frame(window)
frame.pack(padx=20,pady=20)

button1=tk.Button(frame,text="+",command=lambda: add("+"))
button1.grid(row=0,column=0,padx=5,pady=5)

button2=tk.Button(frame,text="-",command=lambda: add("-"))
button2.grid(row=0,column=1,padx=5,pady=5)

#Write code for button 3 here


#Write code for button 4 here


button5=tk.Button(frame,text="=",command=calculate)
button5.grid(row=1,column=1)


answer=tk.Label(window,text="Answer")
answer.pack()
window.mainloop()
