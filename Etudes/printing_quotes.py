# Quote marks are used to show the beginning and end 
# of strings, but sometimes we also want to be able 
# to print them out, by using escape characters.

text, person = input("What is the quote? "), input("Who said it? ")
print(f'{person} says, "{text}"')