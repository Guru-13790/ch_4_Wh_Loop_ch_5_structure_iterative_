def is_prime(number):
    # A number less than or equal to 1 is not prime
    if number <= 1:
        return False
    # Check divisibility from 2 to the square root of the number
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def check_prime():
    try:
        # Ask the user for an integer
        num = int(input("Enter an integer: "))

        # Check if the number is prime
        if is_prime(num):
            print(f"{num} is a prime number.")
        else:
            print(f"{num} is not a prime number.")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")

2
# Run the prime check function
check_prime()
