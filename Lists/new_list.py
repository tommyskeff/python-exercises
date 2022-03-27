mylist = []
running = True

while running:
    item = input("Next item: ")
    if item == "":
        running = False
    else:
        mylist.append(item)

print("\n".join(mylist))
