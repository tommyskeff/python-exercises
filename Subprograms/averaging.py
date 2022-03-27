def average(*numbers):
    return sum(numbers) / len(numbers)


running = True
while running:
    w = float(input('No 1: '))
    x = float(input('No 2: '))
    y = float(input('No 3: '))
    z = float(input('No 4: '))
    mean = average(w, x, y, z)

    print(f"The average of {w} {x} {y} and {z} is {mean}")
    if input("Go again y/n").lower().strip() == "n":
        running = False
