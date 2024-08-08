#Task : Create 1 more radio button and give label non-vegetarian.
import tkinter as tk
root=tk.Tk()
root.title("Radio Buttons")

# Create radio buttons
veg_radio = tk.Radiobutton(root, text="Vegetarian")
veg_radio.pack()
non_veg_radio = tk.Radiobutton(root, text="Non-Vegetarian")
non_veg_radio.pack()

root.mainloop()# Write your code here :-)
