# Using the given list of colours, ask the user 
#   which colour they would like to remove 
#   from the list.
# Remove that colour then print out the revised 
#   list, one item per line
# If the colour is not in the list, 
#   print "Not in list"

colours, i = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"], input("Enter colour to remove: ")
if i in colours:
    colours.remove(i)
    print("\n".join(colours))
else:
    print("Not in list")