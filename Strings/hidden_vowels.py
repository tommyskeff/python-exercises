VOWELS = "aeiou"

string = input("Enter a string: ")
print("".join("*" if char.lower() in VOWELS else char for char in string))
