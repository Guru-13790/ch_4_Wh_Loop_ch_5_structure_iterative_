money = float(input("Enter amount of money: "))
if money>=5:
    print("Y u can buy a latte.")

    age = int(input("Enter your age: "))
    if age >= 65:
        print("You are retired.")
    elif age >= 18:
        print("You are working-age.")
    elif age >= 7:
        print("You are in school.")
    else:
        print("You are a small child.")


first = 1
while first <= 5:
    second = 1
    while second <= 5:
        print(f"{first} times {second} is {first*second:d}")
        second = second + 1
    first = first + 1