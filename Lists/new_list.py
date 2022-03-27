# Sometimes you need to create a new list from scratch.
# Starting with an empty list, write a program that 
#   keeps asking the user for the next item until 
#   they enter nothing.
# Once they enter nothing, print out the entire 
#   list on separate lines.
# Write your code below this point.

mylist = []
running = True

while running:
    item = input("Next item: ")
    if item == "":
        running = False
    else:
        mylist.append(item)
    
print("\n".join(mylist))