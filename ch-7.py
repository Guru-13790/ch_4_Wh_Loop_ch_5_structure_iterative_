from collections import namedtuple

dict1 = {
    "name" : "Alice" ,
    "age" : 25,
    "city" : "Tokyo"
    }
#dict1 = {"name": "Alice", "age": 25, "city": "Tokyo" }

print(dict1)

dict1 = {
    "name": "Alice",
    "age": 25,
    "city": "Tokyo"
}

# Accessing values using keys
name_value = dict1["name"]  # Access the value for the key "name"
age_value = dict1["age"]    # Access the value for the key "age"
city_value = dict1["city"]  # Access the value for the key "city"

print("Name:", name_value)
print("Age:", age_value)
print("City:", city_value)

dict1 = {
    "name": "Alice",
    "age": "26",
    "city": "Tokyo"
}

dict1["surname"] = "Jones"  # Add surname in one line

print(dict1)


    }