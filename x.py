x = 12

user_input = int(input("Guess the value of x: "))

if user_input < x:
    print("x is less than 12")
elif user_input == x:
    print("x is not equal to 12")
elif user_input == x:
    print("Right on the money")
else:
    print("x is greater than 12")

print("The value of x is:", x)