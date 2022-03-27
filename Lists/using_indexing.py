# Using the given list, enter a number
#  and output the selected item from the list
#  eg entering 1 returns red
# Remember indexing starts at zero!

COLOURS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

print(COLOURS[int(input("Enter number: ")) - 1])