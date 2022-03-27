string, i1, i2 = input("String: "), int(input("Index 1: ")), int(input("Index 2: "))
print("\n".join([string[i1:i2], string[:i2], string[i1:]]))
