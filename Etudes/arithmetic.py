# Write a program that prompts for two numbers. 
# Print the sum, difference, product, quotient
# and remainder of those numbers 

first, second = int(input("What is the first number? ")), int(input("What is the second number? "))
print(f"{first} plus {second} equals {first + second}")
print(f"{first} minus {second} equals {first - second}")
print(f"{first} times {second} equals {first * second}")
print(f"{first} divided by {second} equals {first / second}")
print(f"{first} remainder {second} equals {first % second}")