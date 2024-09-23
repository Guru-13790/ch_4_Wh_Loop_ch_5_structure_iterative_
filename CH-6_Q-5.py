# Function to remove odd numbers from a list
def remove_odd_numbers(int_list):
    # Create a new list with only even numbers
    even_list = [num for num in int_list if num % 2 == 0]
    return even_list


# Main program to test the function
def main():
    # Create a list of integers
    original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Call the function to get a list with odd numbers removed
    even_list = remove_odd_numbers(original_list)

    # Print both the original and the modified list
    print("Original list:", original_list)
    print("List with odd numbers removed:", even_list)


# Run the main program
main()
