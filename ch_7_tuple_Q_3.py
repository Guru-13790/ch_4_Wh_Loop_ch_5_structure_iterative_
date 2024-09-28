# Initialize an empty dictionary to store airport data
airports = {}


# Function to enter a new airport
def add_airport():
    icao = input("Enter the ICAO code of the airport: ").upper()  # Uppercase for uniformity
    name = input("Enter the name of the airport: ")

    if icao in airports:
        print(f"The airport with ICAO code {icao} already exists as {airports[icao]}.")
    else:
        airports[icao] = name
        print(f"Airport '{name}' with ICAO code {icao} has been added.")



# Main program loop
def main():
    while True:
        print("\nChoose an option:")
        print("1. Enter a new airport")
        print("2. check for an airport")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            add_airport()
        elif choice == "2":
            check_an_airport()
        elif choice == "3":
            print("Exiting the program. Gooddbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


# Run the main program
main()
