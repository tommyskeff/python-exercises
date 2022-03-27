COLOURS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

i = int(input("Enter number: "))
if i < 1 or i > len(COLOURS):
    print("Not valid")
else:
    print(COLOURS[i - 1])
