#Task : Change the padysize on the line no 30 and observe the change in the code.
import tkinter as tk
from PIL import ImageTk, Image

def display_images(image_dict):
    for i, (food, image_path) in enumerate(image_dict.items()):
        image = Image.open(image_path)
        image = image.resize((150, 100), Image.BILINEAR)
        photo = ImageTk.PhotoImage(image)

        label = tk.Label(frame, image=photo)
        label.image = photo
        label.grid(row=i // 3, column=i % 3, padx=10) #adding three images in one row

food_items = {
    "Burger": "burger.png",
    "Pizza": "pizza.png",
    "Fries": "fries.png",
    "Salad": "salad.png",
    "Biryani": "biryani.png",
    "Pasta": "pasta.png",
    "Sandwich": "sandwich.png",
    "Sushi": "sushi.png",
    "Steak": "steak.png"}

root = tk.Tk()
root.title("Food Ordering App")

frame = tk.Frame(root)
frame.pack(pady=40)

display_images(food_items)

root.mainloop()
