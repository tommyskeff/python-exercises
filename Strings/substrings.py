# Enter a string and two integers
# Print out the substring given by 
#  those two integers as indexes.
#  eg 'apple', 1, 3 outputs 'pp'
# On the next line print the start of 
#  the string to second index
#  eg 'apple', 1, 3 outputs 'app'
# On the last line print out the end
#  of the string from the first index.
#  eg 'apple', 1, 3 outputs 'pple'

string, i1, i2 = input("String: "), int(input("Index 1: ")), int(input("Index 2: "))
print("\n".join([string[i1:i2], string[:i2], string[i1:]]))