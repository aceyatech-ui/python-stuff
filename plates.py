def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(v):
    if not (2 <= len(v) <= 6):
        return False

    if not v[0:2].isalpha():
        return False

    found_number = False
    for i in range(2, len(v)):
        x = v[i]

        if not x.isalnum():
            return False

        if x.isdigit():
            if not found_number and x == '0':
                return False

            found_number = True

        elif found_number:
            if x.isalpha():
                return False


    return True

main()

