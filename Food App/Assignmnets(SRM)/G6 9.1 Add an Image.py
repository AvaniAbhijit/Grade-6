#Task 1 : Change the title of the window to "My Food App"

import tkinter as tk
from PIL import ImageTk, Image  #importing PIL. Execute "pip install Pillow" on shell.

# Create the main window
root = tk.Tk()
root.title("Food Ordering App")

image_path = "burger.png"  #adding name of image
image = Image.open(image_path)  #opening the image
photo = ImageTk.PhotoImage(image)  #converting the image to a format required by tkinter

# Create a label to display the image
label = tk.Label(root, image=photo)  #adding the label to root window
label.image = photo  # Keep a reference to avoid garbage collection
label.pack(pady=20, padx=20)  # Add some padding and display the label

root.mainloop()
