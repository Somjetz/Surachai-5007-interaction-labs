a = float(input("Enter a number: "))
b = float(input("Enter a number: "))
c = a + b

print(f"{a} + {b} = {c}")

print("Writing to file numbers.txt")
print("Reading from file numbers.txt")

with open('numbers.txt', 'w') as file:
    file.write(f"{a} + {b} = {c}")

with open('numbers.txt', 'r') as file:
    data = file.read()
    print(data)