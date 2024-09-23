# Function to collect names
def collect_names():
    names_set = set()  # Use a set to store unique names
    names_list = []  # List to keep the order of names

    while True:
        name = input("Enter a name (or press Enter to quit): ")

        if name == "":
            break  # Exit if the input is an empty string

        if name not in names_set:
            print("New name")
            names_set.add(name)  # Add new name to the set
            names_list.append(name)  # Keep track of the order
        else:
            print("Existing name")

    return names_list


# Main program
def main():
    names = collect_names()

    # Print the list of names
    print("\nList of names entered:")
    for name in names:
        print(name)


# Run the main program
main()
