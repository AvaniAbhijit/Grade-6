#Skip this variation.
import tkinter as tk

def add():
    n1=number1.get() #get the number from 1st entry widget
    answer.config(text=n1) #add both the numbers

def subtract():
    answer.config(text="i perform subtraction")

window=tk.Tk()
window.title("Calculator Application")
window.geometry("400x300")
text=tk.Label(window,text="Calculator")
text.pack()

number1=tk.Entry(window)
number1.pack()

button1=tk.Button(window,text="+",command=add)
button1.pack()
button2=tk.Button(window,text="-",command=subtract)
button2.pack()

answer=tk.Label(window,text="Answer")
answer.pack()
window.mainloop()
