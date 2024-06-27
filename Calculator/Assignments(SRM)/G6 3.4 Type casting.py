#Task 1: Do the type casting for substarct function as well.

import tkinter as tk

def add():
    n1=int(number1.get())
    n2=int(number2.get())
    answer.config(text=n1+n2)

#Add code for substract function here.


window=tk.Tk()
window.title("Calculator Application")
window.geometry("400x300")
text=tk.Label(window,text="Calculator")
text.pack()

number1=tk.Entry(window)
number1.pack()

number2=tk.Entry(window)
number2.pack()

button1=tk.Button(window,text="+",command=add)
button1.pack()
button2=tk.Button(window,text="-")
button2.pack()

answer=tk.Label(window,text="Answer")
answer.pack()
window.mainloop()
