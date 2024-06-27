#Task : Run the code and oberve the changes in the output.
#Add the button2 to the window.
# add the grid code for button on the line no. 33
import tkinter as tk

def add():
    n1=int(number1.get())
    n2=int(number2.get())
    answer.config(text=n1+n2)

def subtract():
    n1=int(number1.get())
    n2=int(number2.get())
    answer.config(text=n1-n2)

window=tk.Tk()
window.title("Calculator Application")
window.geometry("400x300")
text=tk.Label(window,text="Calculator")
text.pack()

number1=tk.Entry(window)
number1.pack()

number2=tk.Entry(window)
number2.pack()

frame=tk.Frame(window) #adding frame
frame.pack()

button1=tk.Button(frame,text="+",command=add) #changing button's parent to frame
button1.grid(row=0,column=1) #specify the element position (0th row 1st column)
button2=tk.Button(frame,text="-",command=subtract) #changing button's parent to frame
                                                 #specify the position (0th row 2nd column)

answer=tk.Label(window,text="Answer")
answer.pack()
window.mainloop()
