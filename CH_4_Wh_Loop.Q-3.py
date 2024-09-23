def find_min_max():
    numbers = []

    while True:
        user_input = input("Enter a number (or press Enter to quit): ")

        if user_input == "":
            break

        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input, please enter a valid number.")

    if numbers:
        smallest = min(numbers)
        largest = max(numbers)
        print(f"Smallest number: {smallest}")
        print(f"Largest number: {largest}")
    else:
        print("No numbers were entered.")

# Run the function
find_min_max()
