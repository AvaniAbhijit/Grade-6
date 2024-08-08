#Task : Create 1 more radio button and give label non-vegetarian.
import tkinter as tk
root=tk.Tk()
root.title("Radio Buttons")

# Create radio buttons
veg_radio = tk.Radiobutton(root, text="Vegetarian")
veg_radio.pack()

root.mainloop()
