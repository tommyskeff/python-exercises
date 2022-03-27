# Using the given list of colours, enter a
#  colour and its replacement.
# Replace the colour in the list of colours.
# Print out the new colour list, one item per line
# Assume the starting colour is alwyays in the list

colours, old_colour, new_colour = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"], input("Colour to replace: "), input("Replacement colour: ")
colours[colours.index(old_colour)] = new_colour

print("\n".join(colours))