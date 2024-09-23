import math


# Function to calculate the unit price of a pizza per square meter
def calculate_unit_price(diameter, price):
    # Calculate the area of the pizza in square meters (π * r^2)
    radius = diameter / 2 / 100  # Convert radius to meters
    area = math.pi * radius ** 2

    # Calculate the price per square meter
    unit_price = price / area
    return unit_price


# Main program to compare two pizzas
def main():
    # Get input for the first pizza
    diameter1 = float(input("Enter the diameter of the first pizza (cm): "))
    price1 = float(input("Enter the price of the first pizza (euros): "))

    # Get input for the second pizza
    diameter2 = float(input("Enter the diameter of the second pizza (cm): "))
    price2 = float(input("Enter the price of the second pizza (euros): "))

    # Calculate unit prices using the function
    unit_price1 = calculate_unit_price(diameter1, price1)
    unit_price2 = calculate_unit_price(diameter2, price2)

    # Print unit prices for comparison
    print(f"Unit price of the first pizza: {unit_price1:.2f} euros per square meter")
    print(f"Unit price of the second pizza: {unit_price2:.2f} euros per square meter")

    # Determine which pizza provides better value
    if unit_price1 < unit_price2:
        print("The first pizza provides better value for money.")
    elif unit_price2 < unit_price1:
        print("The second pizza provides better value for money.")
    else:
        print("Both pizzas provide the same value for money.")


# Run the main program
main()
