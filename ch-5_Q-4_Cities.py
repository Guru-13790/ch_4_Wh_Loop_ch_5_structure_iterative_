def city_list():
    cities = []

    # Collect 5 city names using a for loop
    for i in range(5):
        city = input(f"Enter the name of city {i + 1}: ")
        cities.append(city)

    # Print the city names, one per line, using a for/in loop
    print("\nThe cities you entered are:")
    for city in cities:
        print(city)

# Run the function
city_list()
