#Task 1 : Add button widget to the window and
#text on the button  should be + sign.
#Task 2 : If button is not visible on the screen
#find out the reason behide it. hint of
#code is available in the given code itself.

import tkinter as tk
window=tk.Tk()
window.title("Calculator Application")
window.geometry("400x300")
text=tk.Label(window,text="Calculator")
text.pack()

#write code on next line for button.
#button=tk.Button(window,text="+",command=add)

answer=tk.Label(window,text="Answer")
answer.pack()
window.mainloop()
