def hello():
    name = input("What's your name? ")
    print(f"Hey {name}, I hope you're having a great day!")


running = True
while (running):
    hello()
    if input("Do you want to continue? (y/n) ") == "n":
        running = False
