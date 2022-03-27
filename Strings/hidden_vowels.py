# Letter replacement
# Enter a string.
# The output should be that string
#  with every vowel replaced with
#  an asterisk.
#  eg entering "Forfar Athletic"
#  returns "F*rf*r *thl*t*c"

VOWELS = "aeiou"

string = input("Enter a string: ")
print("".join("*" if char.lower() in VOWELS else char for char in string))