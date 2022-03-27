COLOURS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

colours, running = COLOURS, True
while running:
    colour = input("Enter colour: ")
    if colour:
        colours.append(colour)
    else:
        running = False

print("\n".join(colours))
