#Task: Add more images in the dicitonary food_items.
#"Salad": "salad.png","Biryani": "biryani.png","Pasta": "pasta.png",
#"Sandwich": "sandwich.png","Sushi": "sushi.png","Steak": "steak.png"}

import tkinter as tk
from PIL import ImageTk, Image

# Create the main window
root = tk.Tk()
root.title("Food Ordering App")

# Create a dictionary to hold information about food items
food_items = {
    "burger": "burger.png",
    "pizza": "pizza.png",
    "fries": "fries.png"
}

def display_images(image_dict):
    # Load and display images
    for i, (food, image_path) in enumerate(image_dict.items()):
        image = Image.open(image_path)
        image = image.resize((150, 100), Image.BILINEAR)
        photo = ImageTk.PhotoImage(image)

        label = tk.Label(frame, image=photo)
        label.image = photo
        label.grid()

# Create a frame to contain the images
frame = tk.Frame(root)
frame.pack(pady=20, padx=20)

# Call the display_images function with the food_items dictionary
display_images(food_items)

root.mainloop()
