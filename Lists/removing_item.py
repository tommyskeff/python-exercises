COLOURS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

colours, i = COLOURS, input("Enter colour to remove: ")
if i in colours:
    colours.remove(i)
    print("\n".join(colours))
else:
    print("Not in list")
