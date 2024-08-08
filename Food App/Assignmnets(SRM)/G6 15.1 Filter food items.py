#Task1 : Run the code and see what happens.
#Task2 : Undestand the true and false statements.

# Sample food items list
food_items = [{"name": "Burger", "image_path": "burger.png", "vegetarian": False},
              {"name": "Pizza", "image_path": "pizza.png", "vegetarian": False},
              {"name": "Salad", "image_path": "salad.png", "vegetarian": True},
              {"name": "Biryani", "image_path": "biryani.png", "vegetarian": False}]

for food in food_items:
        filter=[food for food in food_items if food["vegetarian"]] #access each item in the loop, check if it is vegetarian and if the condition satisfies add it inside the list

print(filter)
