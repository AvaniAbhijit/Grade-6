import tkinter as tk
from tkinter import messagebox

def on_button_click(btn_text):
    display.insert(tk.END, btn_text)

def equals():
    expression = display.get()
    result = eval(expression)
    display.delete(0, tk.END)
    display.insert(tk.END, str(result))

def clear():
    display.delete(0, tk.END)

root = tk.Tk()
root.title("Simple Calculator")

display = tk.Entry(root, font=('Arial', 20), bd=10, insertwidth=4, width=15, justify='right')
display.grid(row=0, column=0, columnspan=4)

# Create buttons
btn_7 = tk.Button(root, text='7', font=('Arial', 20), width=3, height=1, command=lambda: on_button_click('7'))
btn_8 = tk.Button(root, text='8', font=('Arial', 20), width=3, height=1, command=lambda: on_button_click('8'))
btn_9 = tk.Button(root, text='9', font=('Arial', 20), width=3, height=1, command=lambda: on_button_click('9'))
btn_divide = tk.Button(root, text='/', font=('Arial', 20), width=3, height=1, command=lambda: on_button_click('/'))

btn_4 = tk.Button(root, text='4', font=('Arial', 20), width=3, height=1, command=lambda: on_button_click('4'))
btn_5 = tk.Button(root, text='5', font=('Arial', 20), width=3, height=1, command=lambda: on_button_click('5'))
btn_6 = tk.Button(root, text='6', font=('Arial', 20), width=3, height=1, command=lambda: on_button_click('6'))
btn_multiply = tk.Button(root, text='*', font=('Arial', 20), width=3, height=1, command=lambda: on_button_click('*'))

btn_1 = tk.Button(root, text='1', font=('Arial', 20), width=3, height=1, command=lambda: on_button_click('1'))
btn_2 = tk.Button(root, text='2', font=('Arial', 20), width=3, height=1, command=lambda: on_button_click('2'))
btn_3 = tk.Button(root, text='3', font=('Arial', 20), width=3, height=1, command=lambda: on_button_click('3'))
btn_subtract = tk.Button(root, text='-', font=('Arial', 20), width=3, height=1, command=lambda: on_button_click('-'))

btn_0 = tk.Button(root, text='0', font=('Arial', 20), width=3, height=1, command=lambda: on_button_click('0'))
btn_dot = tk.Button(root, text='.', font=('Arial', 20), width=3, height=1, command=lambda: on_button_click('.'))
btn_equal = tk.Button(root, text='=', font=('Arial', 20), width=3, height=1, command=equals)
btn_add = tk.Button(root, text='+', font=('Arial', 20), width=3, height=1, command=lambda: on_button_click('+'))
btn_clear = tk.Button(root, text='C', font=('Arial', 20), width=3, height=1, command=clear)

# Place buttons
btn_7.grid(row=1, column=0)
btn_8.grid(row=1, column=1)
btn_9.grid(row=1, column=2)
btn_divide.grid(row=1, column=3)

btn_4.grid(row=2, column=0)
btn_5.grid(row=2, column=1)
btn_6.grid(row=2, column=2)
btn_multiply.grid(row=2, column=3)

btn_1.grid(row=3, column=0)
btn_2.grid(row=3, column=1)
btn_3.grid(row=3, column=2)
btn_subtract.grid(row=3, column=3)

btn_0.grid(row=4, column=0)
btn_dot.grid(row=4, column=1)
btn_equal.grid(row=4, column=2)
btn_add.grid(row=4, column=3)

btn_clear.grid(row=5, column=1)

root.mainloop()
