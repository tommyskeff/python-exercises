COLOURS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

colours, old_colour, new_colour = COLOURS, input("Colour to replace: "), input("Replacement colour: ")
colours[colours.index(old_colour)] = new_colour

print("\n".join(colours))
