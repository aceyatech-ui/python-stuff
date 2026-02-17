def main():
    camel_case = input("Write something in camelCase: ")
    snake_case = convert(camel_case)
    print(snake_case)

def convert(name):
    result = ""

    for x in name:
        if x.isupper():
            result += "_" + x.lower()

        else:
            result += x

    return result

main()