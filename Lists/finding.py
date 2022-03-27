# Using the given list, enter an item.
# If the item is in the list, print "FOUND"
# If the item is not in the list, print "Not found"

COLOURS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

item = input("Enter colour: ")
print("FOUND" if item.lower() in COLOURS else "Not found")