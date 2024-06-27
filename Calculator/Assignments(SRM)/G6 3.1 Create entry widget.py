#Task : Obseve the line no 6,7,18 & 19 code and create the second entry widget.

import tkinter as tk

def add():
    n1=number1.get() #get the number from the entry widget
    answer.config(text=n1) #display the answer in the label

def subtract():
    answer.config(text="I perform subtraction")

window=tk.Tk()
window.title("Calculator Application")
window.geometry("400x300")
text=tk.Label(window,text="Calculator")
text.pack()

number1=tk.Entry(window) #create an entry widget
number1.pack() #add the entry widget to the window

button1=tk.Button(window,text="+",command=add)
button1.pack()
button2=tk.Button(window,text="-",command=subtract)
button2.pack()

answer=tk.Label(window,text="Answer")
answer.pack()
window.mainloop()
