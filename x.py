x = 12

user_input = int(input("Guess the value of x: "))

if user_input < x:
    print("x is greater than your guess")
elif user_input == x:
    print("Right on the money")
elif user_input > x:
    print("x is less than your guess")
else:
    print("x is greater than 12")
