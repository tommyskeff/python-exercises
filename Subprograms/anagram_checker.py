def isAnagram(first, second):
    return sorted(first) == sorted(second)


print("Enter two strings and I'll tell you if they are anagrams:")
first, second = input("Enter the first string: "), input("Enter the second string: ")
print(f'"{first}" and "{second}" are{"" if isAnagram(first, second) else " not"} anagrams')
