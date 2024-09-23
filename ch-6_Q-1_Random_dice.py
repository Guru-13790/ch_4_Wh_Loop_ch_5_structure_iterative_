import random

# Function to simulate a dice roll
def roll_dice():
    return random.randint(1, 6)  # Random integer between 1 and 6

# Main program to roll the dice until a 6 is rolled
def main():
    roll = 0
    while roll != 6:
        roll = roll_dice()
        print(f"Rolled: {roll}")

# Run the main program
main()
