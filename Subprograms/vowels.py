# Edit the code so that the code sequence that 
# processes the data is a single function. Your 
# function should be called vowelPC(), and should 
# take one parameter, a string, and return one 
# value, a float, that is the percentage of vowels 
# in the string. Amend the main program to use 
# vowelPC() rather than the code block currently 
# being used.

def vowelPC(name):
    vowelcount = sum([1 if letter.lower() in "aeiou" else 0 for letter in name])
    return 100 * vowelcount / len(name)

running = True
while running:
    name = input("What is your name? ").strip().title()
    if name == "":
        running = False
    else:
        print(f"Your name is {vowelPC(name):.1f}% vowels")

print("Bye!")
