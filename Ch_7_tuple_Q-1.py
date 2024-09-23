# Define the seasons as a tuple
seasons = ("Winter", "Spring", "Summer", "Autumn")


# Function to get the season based on the month number
def get_season(month):
    if month in (12, 1, 2):
        return seasons[0]  # Winter
    elif month in (3, 4, 5):
        return seasons[1]  # Spring
    elif month in (6, 7, 8):
        return seasons[2]  # Summer
    elif month in (9, 10, 11):
        return seasons[3]  # Autumn
    else:
        return None  # Invalid month


# Main program
def main():
    try:
        # Ask the user to enter the number of a month
        month = int(input("Enter the number of a month (1-12): "))

        # Get the season based on the month
        season = get_season(month)

        # Check if the input is valid and print the corresponding season
        if season:
            print(f"The corresponding season is: {season}")
        else:
            print("Invalid month. Please enter a number between 1 and 12.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")


# Run the main program
main()
