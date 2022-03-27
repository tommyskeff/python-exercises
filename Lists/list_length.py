# Using the given list, enter a number
#  and output the selected item from the list
#  eg entering 1 returns red
# Remember indexing starts at zero!
# Using length of the list, check if the entered
#  number is a valid index number.
#  If it isn't, output "Not valid"

COLOURS = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

i = int(input("Enter number: "))
if i < 1 or i > len(COLOURS):
    print("Not valid")
else:
    print(COLOURS[i - 1])