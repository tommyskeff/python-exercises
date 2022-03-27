# Using the given list of colours, 
#  enter a new colour and add it 
#  to the end of the list.
# Keep entering new colours until nothing
#  is entered (ie return key is pressed 
#  without typing anything).
# Then print out the new list, one item per line

COLOURS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

colours, running = COLOURS, True
while running:
    colour = input("Enter colour: ")
    if colour:
        colours.append(colour)
    else:
        running = False

print("\n".join(colours))