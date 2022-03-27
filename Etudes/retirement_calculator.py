import datetime

age, retire_age = int(input("What is your current age? ")), int(input("At what age would you like to retire? "))
year, left = datetime.datetime.now().year, retire_age - age

print(f"You have {left} years left until you can retire.")
print(f"It is {year}, so you can retire in {year + left}.")
