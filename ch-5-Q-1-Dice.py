import random


def roll_dice():
    # Ask the user how many dice to roll
    try:
        num_dice = int(input("How many dice would you like to roll? "))

        if num_dice <= 0:
            print("Please enter a positive number of dice.")
            return

        total_sum = 0

        # Roll each die and add to the total sum
        for _ in range(num_dice):
            roll = random.randint(1, 6)  # Simulate rolling a 6-sided die
            total_sum += roll

        # Print the result
        print(f"The sum of the dice rolls is: {total_sum}")

    except ValueError:
        print("Invalid input. Please enter a valid number.")


# Run the dice rolling function
roll_dice()
