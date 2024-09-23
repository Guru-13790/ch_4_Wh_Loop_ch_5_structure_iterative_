import random


def guessing_game():
    # Generate a random number between 1 and 10
    number_to_guess = random.randint(1, 10)

    print("I have drawn a number between 1 and 10. Try to guess it!")

    while True:
        user_input = input("Enter your guess: ")

        try:
            guess = int(user_input)
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 10.")
            continue

        if guess < 1 or guess > 10:
            print("Out of range! Please guess a number between 1 and 10.")
        elif guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print("Correct! You guessed the right number.")
            break


# Run the game
guessing_game()
