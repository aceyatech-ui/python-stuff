found = False

user_guess = print(input("Guess a number from 1 to 30: "))

guess = [3, 5, 7, 11, 23]

for value in guess: 
    if value == user_guess:
        found = True
        print("Found!")

    elif value not in guess:
        print(f"Wrong! {user_guess} is invalid")

print(f"Found: {found}, the number {user_guess} is in the list.")