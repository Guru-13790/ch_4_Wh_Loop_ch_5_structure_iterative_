dict1 = {
    "name": "Alice",
    "age": "26",
    "city": "Tokyo"
}

dict1["surname"] = "Jones"  # Add surname in one line

# Add a numeric key
dict1[1] = "Some Value"  # You can replace "Some Value" with any value you want

# Print the entire dictionary
print(dict1)

# Remove an item using pop
surname_value = dict1.pop("surname")  # Removes the key "surname" and returns its value

# Print the updated dictionary and the removed value
print(dict1)
print("Removed surname:", surname_value)

# Example dictionary
dict1 = {
    "name": "Alice",
    "age": "26",
    "city": "Tokyo",
    "surname": "Jones"
}

# Ask user for a string
mykey = input("Please give me a string: ")

# Check if the user's string is a key in the dictionary
if mykey in dict1:
    print(f"'{mykey}' is a key in this dictionary.")
else:
    print(f"'{mykey}' is not a key in this dictionary.")
