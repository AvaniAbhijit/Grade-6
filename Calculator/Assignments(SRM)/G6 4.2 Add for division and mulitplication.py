#Task1 : Add the button for multiplication and division on the window.
#    Add the grid as well for those button on the specify lines.
#Task2 : Write the function for the same. Give function name multiply and divide.

import tkinter as tk

def add():
    n1=int(number1.get())
    n2=int(number2.get())
    answer.config(text=n1+n2)

def subtract():
    n1=int(number1.get())
    n2=int(number2.get())
    answer.config(text=n1-n2)

#Add the multipl function code on below lines




#Add the divide function code on below lines




window=tk.Tk()
window.title("Calculator Application")
window.geometry("400x300")
text=tk.Label(window,text="Calculator")
text.pack()

number1=tk.Entry(window)
number1.pack()

number2=tk.Entry(window)
number2.pack()
frame=tk.Frame(window)
frame.pack()

button1=tk.Button(frame,text="+",command=add)
button1.grid(row=0,column=1)
button2=tk.Button(frame,text="-",command=subtract)
button2.grid(row=0,column=2)
#Add the button 3 code on the below line


#Add the button 4 code on the below line



answer=tk.Label(window,text="Answer")
answer.pack()
window.mainloop()
