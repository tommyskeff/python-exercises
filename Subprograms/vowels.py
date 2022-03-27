def vowel_percentage(name):
    return 100 * sum([1 if letter.lower() in "aeiou" else 0 for letter in name]) / len(name)


running = True
while running:
    name = input("What is your name? ")
    if name == "":
        running = False
    else:
        print(f"Your name is {vowel_percentage(name):.1f}% vowels")

print("Bye!")
