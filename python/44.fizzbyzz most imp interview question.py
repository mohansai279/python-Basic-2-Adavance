
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzBYZZ")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Byzz")
    else:
        print(i)

