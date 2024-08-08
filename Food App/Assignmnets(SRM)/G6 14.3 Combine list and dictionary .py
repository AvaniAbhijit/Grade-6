#Task 1: Create an list name fruits and
#add the food name with values into dicitonary.
# Task 2: Access the name of the first dicitonary and print it.

food=[{"name":"Burger","image_path":"burger.png","vegetarian":False},
     {"name": "Pizza", "image_path": "pizza.png", "vegetarian": False}] #adding details about one food item inside one dictionary.
     #combinging all these dictionaries using a list

print(food[0]["name"])  #accessing the name of first dictionary
print(food[1]["image_path"])  #accessing the image_path of second dictionary
