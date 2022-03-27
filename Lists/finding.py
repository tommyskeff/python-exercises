COLOURS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

item = input("Enter colour: ")
print("FOUND" if item.lower() in COLOURS else "Not found")
