#Task1 : Change label to "Calculator"
#Task2 : Change geometry dimension of the window.

import tkinter as tk

window = tk.Tk()
window.title("Heading")
window.geometry("400x300")
text = tk.Label(window, text="Title of your application")
text.pack()

window.mainloop()
