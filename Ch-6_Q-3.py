# Function to convert gallons to liters
def gallons_to_liters(gallons):
    liters = gallons * 3.78541  # 1 gallon = 3.78541 liters
    return liters


# Main program to get user input and convert gallons to liters
def main():
    while True:
        try:
            gallons = float(input("Enter volume in gallons (negative value to quit): "))

            if gallons < 0:
                print("Exiting the program.")
                break  # Stop the program if negative input is given

            liters = gallons_to_liters(gallons)
            print(f"{gallons} gallons is equal to {liters:.2f} liters.")

        except ValueError:
            print("Invalid input. Please enter a numeric value.")


# Run the main program
main()
