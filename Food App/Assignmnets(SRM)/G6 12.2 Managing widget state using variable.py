#Task : Assign the int variable to non vegetarian radio button
import tkinter as tk

root = tk.Tk()
root.title("Radio Buttons")

radio_var = tk.IntVar(
)  #creating variable to manage the state of radio buttons

veg_radio = tk.Radiobutton(root, text="Vegetarian",
    variable=radio_var)  #assign the int variable to this radio button
veg_radio.pack()

root.mainloop()
