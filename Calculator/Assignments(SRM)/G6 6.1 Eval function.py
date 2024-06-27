#Task : Run the code and find out the changes when you click on + or - buttons.

import tkinter as tk
from tkinter import messagebox

def check():
    if number1.get()=="":
        messagebox.showinfo("Error","Fields are empty")
    else:
        return

def calculate():
    answer.config(text=eval(number1.get())) #using eval to calculate the expression written on the entry field.

def add(text): #this function takes the parameter from button press and adds it on the entry field (For eg: when + is clicked the + symbol will be added)
    number1.insert(tk.END,text) #insert() method is used to add the value. tk.END tells the computer to add the symbol at the end of expression that has been entered so far. (For eg: if user has eneterd 24 and clicks on +, tk.END adds + at the end of 24 like 24+)

window=tk.Tk()
window.title("Calculator Application")
window.geometry("400x300")
text=tk.Label(window,text="Calculator")
text.pack()

number1=tk.Entry(window)
number1.pack(padx=5,pady=5)

frame=tk.Frame(window)
frame.pack(padx=20,pady=20)

button1=tk.Button(frame,text="+",command=lambda: add("+")) #using lambda function to pass the symbol "+" to the add() function.
button1.grid(row=0,column=1,padx=5,pady=5)

button2=tk.Button(frame,text="-",command=lambda: add("-"))#using lambda function to pass the symbol "-" to the add() function itself.
button2.grid(row=0,column=2,padx=5,pady=5)

button5=tk.Button(frame,text="=",command=calculate)
button5.grid(row=1,column=1)


answer=tk.Label(window,text="Answer")
answer.pack()
window.mainloop()
