#Task : Add two more images to the app.
#Add pizza and fries images and add them to frame as well.
import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Food Ordering App")

# Create a frame to contain the images
frame = tk.Frame(root)
frame.pack(pady=20, padx=20)


image_path = "burger.png"
image_path = "pizza.png"
image_path = "fries.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = tk.Label(frame, image=photo) #adding image inside the frame
label.image = photo
label.pack(pady=20, padx=20)


# Create a frame to contain the buttons
image_path = "burger.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = tk.Label(frame, image=photo) #adding image inside the frame
label.image = photo
label.pack(pady=20, padx=20)
image_path = "pizza.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = tk.Label(frame, image=photo) #adding image inside the frame
label.image = photo
label.pack(pady=20, padx=20)
image_path = "fries.png"
image = Image.open(image_path)
photo = ImageTk.PhotoImage(image)
label = tk.Label(frame, image=photo) #adding image inside the frame
label.image = photo
label.pack(pady=20, padx=20)

root.mainloop()
