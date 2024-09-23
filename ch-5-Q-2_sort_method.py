def find_top_five_numbers():
    numbers = []

    # Loop to get user input
    while True:
        user_input = input("Enter a number (or press Enter to quit): ")

        if user_input == "":
            break

        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input, please enter a valid number.")

    # Check if there are any numbers
    if numbers:
        # Sort the list in descending order and get the top 5 numbers
        numbers.sort(reverse=True)
        top_five = numbers[:5]

        print(f"The five greatest numbers are: {top_five}")
    else:
        print("No numbers were entered.")

# Run the function
find_top_five_numbers()
