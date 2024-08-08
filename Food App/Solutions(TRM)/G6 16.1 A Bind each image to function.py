import tkinter as tk
from PIL import ImageTk, Image

def update_images():
    selection = radio_var.get()

    # Clear existing images from the frame
    for widget in frame.winfo_children():
        widget.destroy()

    filtered_food_items = []

    if selection == 1:  # Vegetarian
        for food in food_items:
            if food["vegetarian"]:
                filtered_food_items.append(food)
    elif selection == 2:  # Non-Vegetarian
        for food in food_items:
            if not food["vegetarian"]:
                filtered_food_items.append(food)
    else:  # Both
        filtered_food_items = food_items

    display_images(filtered_food_items)


def display_images(image_list):
    for i, food in enumerate(image_list):
        image = Image.open(food["image_path"])
        image = image.resize((150, 100), Image.BILINEAR)
        photo = ImageTk.PhotoImage(image)

        # Display image
        image_label = tk.Label(frame, image=photo)
        image_label.image = photo
        image_label.grid(row=i // 3 * 2, column=i % 3, padx=10, pady=5)

        # Display food name below the image
        name_label = tk.Label(frame, text=food["name"])
        name_label.grid(row=i // 3 * 2 + 1, column=i % 3, padx=10, pady=5)

        # Bind the image label to a function that shows the details popup
        image_label.bind("<Button-1>", lambda event, food=food: show_details_popup(food))


def show_details_popup(food):
    popup = tk.Toplevel()
    popup.title(food["name"])
    tk.Label(popup, text=f"Name: {food['name']}").pack()
    tk.Label(popup, text=f"Vegetarian: {'Yes' if food['vegetarian'] else 'No'}").pack()
    tk.Button(popup, text="Close", command=popup.destroy).pack(pady=10)


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

# Create a frame for the radio buttons
radio_frame = tk.Frame(root)
radio_frame.pack(pady=10)

# Create the radio buttons and place them in the radio_frame
radio_var = tk.IntVar(value=3)
veg_radio = tk.Radiobutton(radio_frame, text="Vegetarian", variable=radio_var, value=1, command=update_images)
nonveg_radio = tk.Radiobutton(radio_frame, text="Non-Vegetarian", variable=radio_var, value=2, command=update_images)
both_radio = tk.Radiobutton(radio_frame, text="Both", variable=radio_var, value=3, command=update_images)

veg_radio.pack(side=tk.LEFT, padx=5)
nonveg_radio.pack(side=tk.LEFT, padx=5)
both_radio.pack(side=tk.LEFT, padx=5)

# Create a frame for the images
frame = tk.Frame(root)
frame.pack(pady=20)

# Initially display all images
display_images(food_items)

root.mainloop()
