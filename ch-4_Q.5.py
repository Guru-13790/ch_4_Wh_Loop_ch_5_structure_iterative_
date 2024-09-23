def login_system():
    correct_username = "python"
    correct_password = "rules"
    max_attempts = 5
    attempts = 0

    while attempts < max_attempts:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == correct_username and password == correct_password:
            print("Welcome!")
            break
        else:
            attempts += 1
            if attempts < max_attempts:
                print(f"Incorrect username or password. You have {max_attempts - attempts} attempts left.")
            else:
                print("Access denied.")

# Run the login system
login_system()
