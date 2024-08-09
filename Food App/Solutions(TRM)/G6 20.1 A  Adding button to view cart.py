import tkinter as tk
from PIL import ImageTk, Image
from tkinter import messagebox

food_prices = {
    "Burger": 5.99,
    "Pizza": 8.99,
    "Fries": 2.49,
    "Salad": 6.99,
    "Biryani": 10.99,
    "Pasta": 7.49,
    "Sandwich": 4.99,
    "Sushi": 9.99,
    "Steak": 12.99
}

cart = []

def update_images():
    selection = radio_var.get()
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

        label.bind("<Button-1>", lambda event, food=food: show_details_popup(food))

def show_details_popup(food):
    popup = tk.Toplevel()
    popup.title("Food Details")
    image = Image.open(food["image_path"])
    image = image.resize((250, 200), Image.BILINEAR)
    photo = ImageTk.PhotoImage(image)

    label = tk.Label(popup, image=photo)
    label.image = photo
    label.pack()

    name_label = tk.Label(popup, text=food["name"], font=("Arial", 16, "bold"))
    name_label.pack(pady=10)

    quantity_label = tk.Label(popup, text="Quantity:")
    quantity_label.pack()
    quantity_entry = tk.Entry(popup)
    quantity_entry.pack()

    special_requests_label = tk.Label(popup, text="Special Requests:")
    special_requests_label.pack()

    extra_cheese_var = tk.IntVar()
    no_onions_var = tk.IntVar()
    extra_sauce_var = tk.IntVar()

    extra_cheese_checkbox = tk.Checkbutton(popup, text="Extra Cheese", variable=extra_cheese_var)
    extra_cheese_checkbox.pack()

    no_onions_checkbox = tk.Checkbutton(popup, text="No Onions", variable=no_onions_var)
    no_onions_checkbox.pack()

    extra_sauce_checkbox = tk.Checkbutton(popup, text="Extra Sauce", variable=extra_sauce_var)
    extra_sauce_checkbox.pack()

    add_to_cart_button = tk.Button(popup, text="Add to Cart", command=lambda: add_to_cart(food, quantity_entry.get(), extra_cheese_var.get(), no_onions_var.get(), extra_sauce_var.get()))
    add_to_cart_button.pack(pady=10)

    close_button = tk.Button(popup, text="Close", command=popup.destroy)
    close_button.pack(pady=10)

def add_to_cart(food, quantity, extra_cheese, no_onions, extra_sauce):
    if quantity.isdigit() and int(quantity) > 0:
        special_requests = []
        if extra_cheese:
            special_requests.append("Extra Cheese")
        if no_onions:
            special_requests.append("No Onions")
        if extra_sauce:
            special_requests.append("Extra Sauce")

        cart.append({"name": food["name"], "quantity": int(quantity), "price": food_prices[food["name"]], "special_requests": special_requests})
        print(f"Added {quantity} {food['name']} to cart with special requests: {special_requests}")
    else:
        messagebox.showinfo("Error", "Enter a positive integer")

def view_cart():
    cart_window = tk.Toplevel()
    cart_window.title("Cart")

    if not cart:
        label = tk.Label(cart_window, text="Your cart is empty.", font=("Arial", 14))
        label.pack(pady=20)
    else:
        for item in cart:
            item_text = f"{item['quantity']} x {item['name']} @ ${item['price']} each"
            if item['special_requests']:
                item_text += f" (Special requests: {', '.join(item['special_requests'])})"
            label = tk.Label(cart_window, text=item_text, font=("Arial", 12))
            label.pack(pady=5)

    close_button = tk.Button(cart_window, text="Close", command=cart_window.destroy)
    close_button.pack(pady=10)

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

veg_radio = tk.Radiobutton(frame, text="Vegetarian", variable=radio_var, value=1, command=update_images)
nonveg_radio = tk.Radiobutton(frame, text="Non-Vegetarian", variable=radio_var, value=2, command=update_images)
both_radio = tk.Radiobutton(frame, text="Both", variable=radio_var, value=3, command=update_images)

veg_radio.grid(row=5, column=0, padx=5)
nonveg_radio.grid(row=5, column=1, padx=5)
both_radio.grid(row=5, column=2, padx=5)

# Create View Cart button
view_cart_button = tk.Button(root, text="View Cart", command=view_cart, bg="black", fg="white")
view_cart_button.pack(pady=10)

display_images(food_items)

root.mainloop()
