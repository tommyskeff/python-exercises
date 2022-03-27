# Enter a string and output it in
#  all lower case, all upper case and in
#  and title case (where each word starts
#  upper case and is followed by lower case).
# Each output should be on a separate line

string = input("Text: ")
print("\n".join([string.lower(), string.upper(), string.title()]))