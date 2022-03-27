string, index = input("Enter string: "), int(input("Index: "))
if index >= len(string):
    print("Index too high")
else:
    print(string[index])
