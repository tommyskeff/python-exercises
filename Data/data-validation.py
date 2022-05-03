# Data: Validation

############################################
## TASK 1 - range check ####################
############################################
print("TASK 1 =================")
validNum = False
userNum = 0
prompt = "Enter a number from 1 to 10: "
errMsg = "Not a valid number. Try again"
# Add your code here

while not validNum:
  try:
    userNum = int(input(prompt))
    if userNum >= 1 and userNum <= 10:
      validNum = True
  except:
    pass

  if not validNum:
    print(errMsg)

  

# Your code stops here
print("You are user {}.".format(userNum))
print()



############################################
## TASK 2 - length check ###################
############################################
print("\nTASK 2 =================")
POSTCODE_MIN = 6
POSTCODE_MAX = 8
prompt = "Enter a postcode: "
successMsg = "Valid postcode"
errMsg = "Invalid postcode"
# Add your code here

validPostcode = False
userPostcode = ""

while not validPostcode:
  userPostcode = input(prompt)
  if len(userPostcode) >= 6 and len(userPostcode) <= 8:
    print(successMsg)
    validPostcode = True
  else:
    print(errMsg)

# Your code stops here



############################################
## TASK 3 - presence check #################
############################################
print("\nTASK 3 =================")
userName = ""
prompt = "Enter your name: "
errMsg = "No name entered. Try again"
# Add your code here

while not userName:
  userName = input(prompt)
  if not userName:
    print(errMsg)
    

# Your code stops here
print("Your name is " + userName + ".")
print()



############################################
# Task 4 - look-up check ###################
############################################
print("\nTASK 4 =================")

def isValid(fruit):
    fruits = ['apple', 'banana', 'cherry', 'damson', 'elderberry', 'fig']
  
    return fruit in fruits
  
fruit = input("Enter a fruit: ").strip().lower()
if isValid(fruit):
  print("Is a fruit")
else:
  print("Is not a fruit")
print()



############################################
# Task 5 - menus ###########################
############################################
print("\nTASK 5 =================")
validChoice = False
userChoice = 0
errMsg = "Not a menu option"

def showMenu():
  print("Option 1: Find the highest value")
  print("Option 2: Find the lowest value")
  print("Option 3: Find the average value")

# Add your code here

showMenu()
while not validChoice:
  try:
    userChoice = int(input("Select option: "))
    if userChoice >= 1 and userChoice <= 3:
      validChoice = True
    else:
      raise ValueError()
  except:
    print(errMsg)
  
  

# Your code stops here
print("You entered option {}".format(userChoice))
print()



############################################
# Task 6 - Patterns - letters only #########
############################################
print("\nTASK 6 =================")
MIN_NAME = 1
MAX_NAME = 20
firstName = ""
validName = False
prompt = "Enter your first name: "
errLength="Your name must have 1-20 characters"
errName = "Your name must contain letters only"
successMsg = "Valid first name"
# Add your code here

while not validName:
  firstName = input(prompt)
  if len(firstName) < 1 or len(firstName) > 20:
    print(errLength)
  elif not firstName.isalpha():
    print(errName)
  else:
    validName = True
    print(successMsg)

# Your code stops here



############################################
# Task 7 - Patterns - letters and digits ###
############################################
print("\nTASK 7 =================")
ID_LEN = 4
id = ""
validID = False
prompt = "Enter your ID: "
errLength="Your ID must have 4 characters"
errFirstChar = "First character must be 7,8 or 9"
errLetters = "Last 3 characters must be letters"
successMsg = "Valid ID"
# Add your code here

while not validID:
  id = input(prompt)
  if not len(id) == 4:
    print(errLength)
  elif not id[0] in ["7", "8", "9"]:
    print(errFirstChar)
  elif not id[-3:].isalpha():
    print(errLetters)
  else:
    validID = True
    print(successMsg)

# Your code stops here
