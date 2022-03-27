# Enter two strings
# If the second string is in 
#  the first string, output 'Found'
#  otherwise outout 'Not found'

string1, string2 = input("Target string: "), input("Search string: ")
print("Found" if string2 in string1 else "Not found")