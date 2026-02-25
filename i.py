calc = 0

count = -1


for i in range(10):
    calc = calc + i
    count = count + 1

    print(f"{i}, {calc + i}, {count + i}")
    

print(f"total={calc}")