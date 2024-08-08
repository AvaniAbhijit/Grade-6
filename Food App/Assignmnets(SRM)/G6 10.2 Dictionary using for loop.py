#Task : Crete the dicitonary of your choice values
#and key and print the values of the dictionary using for loop

# Creating a dictionary of friends' names and ages
friends = {
    "Aditya": 25,
    "Bharat": 30,
    "Anay": 28,
    "Saanvi": 27
}

# Use enumerate to access the index and the dictionary item
for index, (name, age) in enumerate(friends.items(), 1):
    print(f"Friend {index}: {name}'s age is {age}.")


