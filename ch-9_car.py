# Define the Car class
class Car:
    # Initializer to set the registration number and maximum speed
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number  # Set registration number
        self.max_speed = max_speed  # Set maximum speed
        self.current_speed = 0  # Set current speed to 0 by default
        self.travelled_distance = 0  # Set travelled distance to 0 by default


# Main program
def main():
    # Create a new car with registration number ABC-123 and maximum speed 142 km/h
    car1 = Car("ABC-123", 142)

    # Print out all the properties of the car
    print(f"Registration Number: {car1.registration_number}")
    print(f"Maximum Speed: {car1.max_speed} km/h")
    print(f"Current Speed: {car1.current_speed} km/h")
    print(f"Travelled Distance: {car1.travelled_distance} km")


# Run the main program
main()


# Define the Car class
class Car:
    # Initializer to set the registration number and maximum speed
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number  # Set registration number
        self.max_speed = max_speed  # Set maximum speed
        self.current_speed = 0  # Set current speed to 0 by default
        self.travelled_distance = 0  # Set travelled distance to 0 by default

    # Method to adjust the car's speed
    def accelerate(self, speed_change):
        # Adjust the speed and ensure it doesn't exceed the max_speed or go below 0
        self.current_speed += speed_change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0


# Main program
def main():
    # Create a new car with registration number ABC-123 and maximum speed 142 km/h
    car1 = Car("ABC-123", 142)

    # Print out the initial properties of the car
    print(f"Registration Number: {car1.registration_number}")
    print(f"Maximum Speed: {car1.max_speed} km/h")
    print(f"Current Speed: {car1.current_speed} km/h")
    print(f"Travelled Distance: {car1.travelled_distance} km")

    # Accelerate the car by 20 km/h
    car1.accelerate(20)
    print(f"\nAfter accelerating by 20 km/h:")
    print(f"Current Speed: {car1.current_speed} km/h")

    # Accelerate the car by another 50 km/h (will be capped at max speed 160 km/h)
    car1.accelerate(30)
    print(f"\nAfter accelerating by 50 km/h (should cap at max speed):")
    print(f"Current Speed: {car1.current_speed} km/h")

    

# Run the main program
main()


