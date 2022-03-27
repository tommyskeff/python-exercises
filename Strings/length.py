string1, string2 = input("First string: "), input("Second string: ")
len1, len2 = len(string1), len(string2)

print(string1 if len1 > len2 else string2)
print(abs(len1 - len2))
