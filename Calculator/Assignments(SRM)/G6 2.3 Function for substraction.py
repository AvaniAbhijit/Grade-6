#Task 1 : Create the function substraction and call
#it so that it can print out the result of the substraction of two numbers.
#Task2 : Create the button 2 and call the function
#substraction so that it can be used as a button to perform the substraction.

import tkinter as tk
def add():
    answer.config(text="I perform addition")

window=tk.Tk()
window.title("Calculator Application")
window.geometry("400x300")
text=tk.Label(window,text="Calculator")
text.pack()

button1=tk.Button(window,text="+",command=add)
button1.pack()

answer=tk.Label(window,text="Answer")
answer.pack()
window.mainloop()
