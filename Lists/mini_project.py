# Write a program that asks the user how many 
#   numbers they are about to enter, and then 
#   lets them enter those numbers and stores 
#   them in a list.
# The program then prints on separate lines 
#   the mean and median of the list of numbers.
# Mean: add the numbers and divide by the 
#   number of numbers
# Median: what number is in the middle of the 
#   sorted list of numbers. If there are an 
#   even number of numbers, print the number 
#   just below the middle.
# Enter your code below here

import statistics

count = int(input("How many numbers? "))
numbers = []

for i in range(count):
    numbers.append(int(input(f"Number {i + 1}: ")))

print("\n".join([f"Mean: {round(statistics.mean(numbers), 1)}", f"Median: {statistics.median_low(numbers)}"]))