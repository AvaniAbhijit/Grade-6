#Task : Change the value on line 33 to see the use of sefault state.
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
frame.pack(pady=20)


radio_var = tk.IntVar(value=3) #adding value as 3 to set default selection


veg_radio = tk.Radiobutton(frame, text="Vegetarian", variable=radio_var, value=1) #add value as 1 for vegetarian
nonveg_radio = tk.Radiobutton(frame, text="Non-Vegetarian", variable=radio_var, value=2) #add value as 2 for non-vegetarian
both_radio = tk.Radiobutton(frame, text="Both", variable=radio_var, value=3) #add value as 3 for both

veg_radio.grid(row=5, column=0, padx=5)
nonveg_radio.grid(row=5, column=1, padx=5)
both_radio.grid(row=5, column=2, padx=5)

display_images(food_items)

root.mainloop()
