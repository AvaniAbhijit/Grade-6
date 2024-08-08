import tkinter as tk
from PIL import ImageTk, Image

def display_images(image_dict):
    for i, (food, image_path) in enumerate(image_dict.items()):
        image = Image.open(image_path)
        image = image.resize((150, 100), Image.BILINEAR)
        photo = ImageTk.PhotoImage(image)

        label = tk.Label(frame, image=photo)
        label.image = photo
        label.grid(row=i // 3, column=i % 3, padx=10)  # Adding three images in one row

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

# Create radio variable
radio_var = tk.IntVar()  # Initially set to both (you can change it later based on your logic)

# Create a frame for radio buttons
radio_frame = tk.Frame(root)
radio_frame.pack(pady=10)

# Create the radio buttons for Vegetarian and Non-Vegetarian
veg_radio = tk.Radiobutton(radio_frame, text="Vegetarian", variable=radio_var, value=1)
veg_radio.pack(side=tk.LEFT, padx=5)

non_veg_radio = tk.Radiobutton(radio_frame, text="Non-Vegetarian", variable=radio_var, value=2)
non_veg_radio.pack(side=tk.LEFT, padx=5)

both_radio = tk.Radiobutton(radio_frame, text="Both", variable=radio_var, value=3)
both_radio.pack(side=tk.LEFT, padx=5)

display_images(food_items)

root.mainloop()
