# Create a program that determines how many years 
# you have left until you can retire (never too 
# early to start planning), and the year you can
# retire.

# The program should prompt for your current age and 
# the age you want to retire.

import datetime

age, retire_age = int(input("What is your current age? ")), int(input("At what age would you like to retire? "))
year, left = datetime.datetime.now().year, retire_age - age

print(f"You have {left} years left until you can retire.")
print(f"It is {year}, so you can retire in {year + left}.")