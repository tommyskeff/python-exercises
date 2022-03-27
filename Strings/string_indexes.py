# Enter a string and the index of a character
# in that string.
# Output the character at that position in the string.
# If the index is too high for the length of string
# output "Index too high"

string, index = input("Enter string: "), int(input("Index: "))
if index >= len(string):
    print("Index too high")
else:
    print(string[index])