import tkinter as tk
from tkinter import ttk, simpledialog, messagebox, IntVar
from PIL import ImageTk, Image
import smtplib
from email.mime.text import MIMEText
import requests

# Global cart list to store selected items
cart = []
cart_window = None
# Dictionary to store food item prices
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

# Create the main window
root = tk.Tk()
root.title("Food Ordering App")


# Function to update the displayed images based on the radio button selection
def update_images():
  selection = radio_var.get()

  # Clear existing images from the frame
  for widget in food_frame.winfo_children():
    widget.destroy()

  filtered_food_items = []

  if selection == 1:  # Display vegetarian only
    for food in food_items:
      if food["vegetarian"]:
        filtered_food_items.append(food)
  elif selection == 2:  # Display non-vegetarian only
    for food in food_items:
      if not food["vegetarian"]:
        filtered_food_items.append(food)
  else:  # Display both
    filtered_food_items = food_items

  display_images(filtered_food_items)


# Function to display images
def display_images(image_list):
  # Load and display images
  for i, food in enumerate(image_list):
    image = Image.open(food["image_path"])
    image = image.resize((150, 100), Image.BILINEAR)
    photo = ImageTk.PhotoImage(image)

    label = tk.Label(food_frame, image=photo)
    label.image = photo
    label.grid(row=i // 3, column=i % 3, padx=10)

    # Bind the image label to a function that shows the details popup
    label.bind("<Button-1>", lambda event, food=food: show_details_popup(food))


# Function to show details popup
def show_details_popup(food):
  popup = tk.Toplevel()
  popup.title("Food Details")

  # Load and display image
  image = Image.open(food["image_path"])
  image = image.resize((250, 200), Image.BILINEAR)
  photo = ImageTk.PhotoImage(image)

  label = tk.Label(popup, image=photo)
  label.image = photo
  label.pack()

  # Display food name
  name_label = tk.Label(popup, text=food["name"], font=("Arial", 16, "bold"))
  name_label.pack(pady=10)

  # Entry for quantity
  quantity_label = tk.Label(popup, text="Quantity:")
  quantity_label.pack()
  quantity_entry = tk.Entry(popup)
  quantity_entry.pack()

  # Checkboxes for special requests
  special_requests_label = tk.Label(popup, text="Special Requests:")
  special_requests_label.pack()

  # IntVars to track the state of checkboxes
  extra_cheese_var = IntVar()
  no_onions_var = IntVar()
  extra_sauce_var = IntVar()

  extra_cheese_checkbox = tk.Checkbutton(popup,
                                         text="Extra Cheese",
                                         variable=extra_cheese_var)
  extra_cheese_checkbox.pack()

  no_onions_checkbox = tk.Checkbutton(popup,
                                      text="No Onions",
                                      variable=no_onions_var)
  no_onions_checkbox.pack()

  extra_sauce_checkbox = tk.Checkbutton(popup,
                                        text="Extra Sauce",
                                        variable=extra_sauce_var)
  extra_sauce_checkbox.pack()

  # Add to cart button
  add_to_cart_button = tk.Button(
      popup,
      text="Add to Cart",
      command=lambda: add_to_cart(food, quantity_entry.get(
      ), extra_cheese_var.get(), no_onions_var.get(), extra_sauce_var.get()))
  add_to_cart_button.pack(pady=10)

  # Close button
  close_button = tk.Button(popup, text="Close", command=popup.destroy)
  close_button.pack(pady=10)


# Function to add item to cart
def add_to_cart(food, quantity, extra_cheese, no_onions, extra_sauce):
  if quantity.isdigit() and int(quantity) > 0:
    special_requests = []
    if extra_cheese:
      special_requests.append("Extra Cheese")
    if no_onions:
      special_requests.append("No Onions")
    if extra_sauce:
      special_requests.append("Extra Sauce")

    cart.append({
        "name": food["name"],
        "quantity": int(quantity),
        "price": food_prices[food["name"]],
        "special_requests": special_requests
    })
    print(
        f"Added {quantity} {food['name']} to cart with special requests: {special_requests}"
    )
  else:
    print("Invalid quantity. Please enter a positive integer.")


# Function to view cart
def view_cart():
  global cart_window
  cart_window = tk.Toplevel()
  cart_window.title("View Cart")

  # Create a Treeview widget for the cart items
  tree = ttk.Treeview(cart_window,
                      columns=('Name', 'Quantity', 'Price', 'Total Price'))
  tree.heading('#0', text='ID')
  tree.heading('Name', text='Name')
  tree.heading('Quantity', text='Quantity')
  tree.heading('Price', text='Price')
  tree.heading('Total Price', text='Total Price')

  if not cart:
    # If cart is empty, display a message
    no_items_label = tk.Label(cart_window,
                              text="Aren't you hungry? Add items quickly")
    no_items_label.pack(pady=10)
  else:
    # Display cart items
    for i, item in enumerate(cart):
      tree.insert('',
                  'end',
                  text=i + 1,
                  values=(item['name'], item['quantity'], item['price'],
                          item['quantity'] * item['price']))

    # Add buttons to edit quantity, add, and remove items
    edit_button = tk.Button(cart_window,
                            text="Edit Quantity",
                            command=lambda: edit_quantity(tree))
    edit_button.pack(pady=5)

    add_button = tk.Button(cart_window,
                           text="Add Item",
                           command=lambda: add_item(tree))
    add_button.pack(pady=5)

    remove_button = tk.Button(cart_window,
                              text="Remove Item",
                              command=lambda: remove_item(tree))
    remove_button.pack(pady=5)

    # Add checkout button
    checkout_button = tk.Button(cart_window,
                                text="Checkout",
                                command=checkout,
                                bg="black",
                                fg="white")
    checkout_button.pack(pady=5)

  tree.pack(expand=True, fill='both')


# Function to edit quantity of selected item
def edit_quantity(tree):
  selection = tree.selection()
  if selection:
    item_id = tree.selection()[0]
    try:
      item_index = int(tree.item(item_id, 'text')) - 1
      quantity_input = simpledialog.askstring(
          "Edit Quantity",
          f"Enter new quantity for item {item_id}: ",
          parent=root)

      if quantity_input is not None and quantity_input.isdigit() and int(
          quantity_input) > 0:
        quantity = int(quantity_input)
        cart[item_index]['quantity'] = quantity
        tree.item(item_id,
                  values=(cart[item_index]['name'], quantity,
                          cart[item_index]['price'],
                          quantity * cart[item_index]['price']))
      else:
        messagebox.showerror(
            "Error", "Invalid quantity. Please enter a positive integer.")
    except ValueError:
      messagebox.showerror("Error", "Invalid item ID.")


# Function to add a new item to the cart
def add_item(tree):
  global cart, cart_window
  root.lift()
  cart_window.destroy()


# Function to remove selected item from the cart
def remove_item(tree):
  selection = tree.selection()
  if selection:
    item_id = selection[0]
    try:
      item_index = int(tree.index(item_id)) - 1
      del cart[item_index]
      tree.delete(item_id)
    except ValueError:
      messagebox.showerror("Error", "Invalid item ID.")


global email_entry, email_popup


# Function to calculate total cost and generate summary
def checkout():
  global email_entry, email_popup
  # Create a popup window for email number entry
  email_popup = tk.Toplevel()
  email_popup.title("Enter Email Id or Phone Number")
  email_popup.geometry("300x250")

  # Label and Entry for email number
  email_label = tk.Label(email_popup,
                         text="Enter your Email Id or Phone Number : ",
                         font=("ariel", "8", "bold"))
  email_label.pack(pady=30)
  email_entry = tk.Entry(email_popup)
  email_entry.pack()

  emailb = tk.Button(email_popup, text="Enter", command=process_checkout)
  emailb.pack()


def sending_sms(summary, rec):
  apiSecret = "23068fce54a81ddfb281dc429258bdcfb5f30dd5"
  deviceId = "00000000-0000-0000-3dcc-f4835d980caa"
  phone = f'+91{rec}'
  message = summary

  message = {
      "secret": apiSecret,
      "mode": "devices",
      "device": deviceId,
      "sim": 1,
      "priority": 1,
      "phone": phone,
      "message": message
  }

  r = requests.post(url="https://www.cloud.smschef.com/api/send/sms",
                    params=message)
  # do something with response object
  result = r.json()

  print(result)


# Function to process checkout after entering email number
def process_checkout():
  global email_entry, summary
  total_cost = sum(item['quantity'] * item['price'] for item in cart)
  summary = "Items Ordered:\n"
  for item in cart:
    summary += f"{item['name']} - Quantity: {item['quantity']}"
    if 'toppings' in item:
      summary += f", Toppings: {', '.join(item['toppings'])}"
    elif 'special_requests' in item:
      summary += f", Special Requests: {', '.join(item['special_requests'])}"
    summary += "\n"
    summary += f"Total Cost: ${total_cost:.2f}\n"
    summary += f"Email Id: {email_entry.get()}"

  # Display the summary
  messagebox.showinfo("Checkout Summary", summary)

  try:  # Checking the user's input
    int(email_entry.get())
    sending_sms(summary, email_entry.get())
  except:
    # Send email
    SendingEmail()


def SendingEmail():
  global email_entry, summary
  sender_email = "avani10.dhatrak@gmail.com"  # Use Your actual Gmail here
  sender_password = "hzey twbz pgjs qxzp"   # Use your actual password here
  recipient_email = email_entry.get()  # Replace with recipient email

  # Construct MIME message
  message = MIMEText(summary)
  message['From'] = sender_email
  message['To'] = recipient_email
  message['Subject'] = "Checkout Summary"

  # Connect to SMTP server
  with smtplib.SMTP('smtp.gmail.com', 587) as server:
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, recipient_email, message.as_string())

  print("Email sent successfully")


# Create a frame to contain the food items
food_frame = tk.Frame(root)
food_frame.pack(pady=20)

# List of food items with their image paths and vegetarian status
food_items = [{
    "name": "Burger",
    "image_path": "Images/pizza.png",
    "vegetarian": False
}, {
    "name": "Pizza",
    "image_path": "Images/pizza.png",
    "vegetarian": False
}, {
    "name": "Fries",
    "image_path": "Images/fries.png",
    "vegetarian": True
}, {
    "name": "Salad",
    "image_path": "Images/salad.png",
    "vegetarian": True
}, {
    "name": "Biryani",
    "image_path": "Images/biryani.png",
    "vegetarian": False
}, {
    "name": "Pasta",
    "image_path": "Images/pasta.png",
    "vegetarian": True
}, {
    "name": "Sandwich",
    "image_path": "Images/sandwich.png",
    "vegetarian": True
}, {
    "name": "Sushi",
    "image_path": "Images/sushi.png",
    "vegetarian": False
}, {
    "name": "Steak",
    "image_path": "Images/steak.png",
    "vegetarian": False
}]

# Create radio variable
radio_var = tk.IntVar(value=3)  # Initially set to both

# Create radio buttons
veg_radio = tk.Radiobutton(root,
                           text="Vegetarian",
                           variable=radio_var,
                           value=1,
                           command=update_images)
nonveg_radio = tk.Radiobutton(root,
                              text="Non-Vegetarian",
                              variable=radio_var,
                              value=2,
                              command=update_images)
both_radio = tk.Radiobutton(root,
                            text="Both",
                            variable=radio_var,
                            value=3,
                            command=update_images)

# Place radio buttons
veg_radio.pack(side=tk.LEFT, padx=5)
nonveg_radio.pack(side=tk.LEFT, padx=5)
both_radio.pack(side=tk.LEFT, padx=5)

# Create View Cart button
view_cart_button = tk.Button(root,
                             text="View Cart",
                             command=view_cart,
                             bg="black",
                             fg="white")
view_cart_button.pack(pady=10)

# Display images initially
update_images()

# Run the main event loop
root.mainloop()
