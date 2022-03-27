# Using the given list, print out each 
#  item on a separate line, omitting green

COLOURS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

for colour in COLOURS:
    if not colour == "green":
        print(colour)