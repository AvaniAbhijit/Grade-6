#Task 1:Change the layout to make the radio buttons
#appear above the images instead of below?
#Task 2: Add a label that displays the name of each food
#item below its corresponding image?

import tkinter as tk
from PIL import ImageTk, Image

def update_images():
   selection = radio_var.get()

# Clear existing images from the frame
   for widget in frame.winfo_children():
      widget.destroy()

   filtered_food_items = []

   if selection == 1:
     for food in food_items:
        if food["vegetarian"]:
            filtered_food_items.append(food)
   elif selection == 2:
     for food in food_items:
        if not food["vegetarian"]:
            filtered_food_items.append(food)
   else:
     filtered_food_items = food_items

   display_images(filtered_food_items)


def display_images(image_list):

    for i, food in enumerate(image_list):
        image = Image.open(food["image_path"])
        image = image.resize((150, 100), Image.BILINEAR)
        photo = ImageTk.PhotoImage(image)

        label = tk.Label(frame, image=photo)
        label.image = photo
        label.grid(row=i // 3, column=i % 3, padx=10)

     # Bind the image label to a function that shows the details popup
        label.bind("<Button-1>", lambda event, food=food: show_details_popup(food))



food_items = [
    {"name": "Burger", "image_path": "burger.png", "vegetarian": False},
    {"name": "Pizza", "image_path": "pizza.png", "vegetarian": False},
    {"name": "Fries", "image_path": "fries.png", "vegetarian": True},
    {"name": "Salad", "image_path": "salad.png", "vegetarian": True},
    {"name": "Biryani", "image_path": "biryani.png", "vegetarian": False},
    {"name": "Pasta", "image_path": "pasta.png", "vegetarian": True},
    {"name": "Sandwich", "image_path": "sandwich.png", "vegetarian": True},
    {"name": "Sushi", "image_path": "sushi.png", "vegetarian": False},
    {"name": "Steak", "image_path": "steak.png", "vegetarian": False}
]


root = tk.Tk()
root.title("Food Ordering App")

frame = tk.Frame(root)
frame.pack(pady=20)


radio_var = tk.IntVar(value=3)

veg_radio = tk.Radiobutton(frame, text="Vegetarian", variable=radio_var, value=1,command=update_images)
nonveg_radio = tk.Radiobutton(frame, text="Non-Vegetarian", variable=radio_var, value=2,command=update_images) #add value as 2 for non-vegetarian
both_radio = tk.Radiobutton(frame, text="Both", variable=radio_var, value=3,command=update_images) #add value as 3 for both

veg_radio.grid(row=5, column=0, padx=5)
nonveg_radio.grid(row=5, column=1, padx=5)
both_radio.grid(row=5, column=2, padx=5)

display_images(food_items)

root.mainloop()
