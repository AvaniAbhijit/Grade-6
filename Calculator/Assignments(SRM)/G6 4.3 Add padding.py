#Task : Add the padding for number2 entry widget,frame,
#button 1 to button4 and frame.
import tkinter as tk

def add():
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
number1.pack(padx=5,pady=5)#pady adds padding to the entry box to distance it from the label on top and second entry box in the bottom using padx. A padx is used to add padding to the entry box on the sides.

number2=tk.Entry(window)
number2.pack()

frame=tk.Frame(window)
frame.pack()

button1=tk.Button(frame,text="+",command=add)
button1.grid(row=0,column=1) #adding padding to increase distance between buttons
button2=tk.Button(frame,text="-",command=subtract)
button2.grid(row=0,column=2) #adding padding to increase distance between buttons
button3=tk.Button(frame,text="*",command=multiply)
button3.grid(row=0,column=3) #adding padding to increase distance between buttons
button4=tk.Button(frame,text="/",command=divide)
button4.grid(row=0,column=4) #adding padding to increase distance between buttons

answer=tk.Label(window,text="Answer")
answer.pack()
window.mainloop()
