x = int(input("Enter the value for x: "))
y = int(input("Enter the value for y: "))

while y != 0:
    if x > y: 
        x = x - y
    else:
        y = y - x

print("Result:", x)
