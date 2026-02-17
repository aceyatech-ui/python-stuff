user_says = input(" ")

vowels = "aeiouAEIOU"

result = ""
for x in user_says:
    if x not in vowels:
        result += x

print(result)