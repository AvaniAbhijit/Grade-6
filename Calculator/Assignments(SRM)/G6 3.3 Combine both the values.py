#Task1 : Run the program and see what happens.
#Why it is not adding the number from the text widget 1 & 2.


import tkinter as tk

def add():
    n1=number1.get()
    n2=number2.get()
    answer.config(text=n1+n2)

def subtract():
    answer.config(text="i perform subtraction")

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
button2=tk.Button(window,text="-",command=subtract)
button2.pack()

answer=tk.Label(window,text="Answer")
answer.pack()
window.mainloop()
