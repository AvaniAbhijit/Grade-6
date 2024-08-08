#Task 1: Create 1 more checkbox and add it on window.
import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Checkbox Example")

# Create checkboxes and add them to the list
var1 = tk.IntVar()
checkbox1 = tk.Checkbutton(root, text="Checkbox 1", variable=var1)
checkbox1.pack(anchor=tk.W)

var2 = tk.IntVar()
checkbox2 = tk.Checkbutton(root, text="Checkbox 2", variable=var2)
checkbox2.pack(anchor=tk.W)

var3 = tk.IntVar()
checkbox3 = tk.Checkbutton(root, text="Checkbox 3", variable=var3)
checkbox3.pack(anchor=tk.W)

# Run the main event loop
root.mainloop()
