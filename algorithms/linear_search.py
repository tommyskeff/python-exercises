# Algorithms: Linear Search

def linearSearch(searchItem,array):
  found = False

  # Your TASK 1 code below here
  
  for item in array:
    if item == searchItem:
      found = True
  
  return found

def linearTableSearch(searchItem,table):
  found = False
  # Your TASK 2 code below here

  for array in table:
    if linearSearch(searchItem, array):
      found = True
  
  return found

###################################
# EDIT NOTHING AFTER THIS COMMENT #
###################################

def _openData(filename,*,dim=1):
    data = []
    with open(filename, 'r') as f:
        for line in f:
            if dim == 1:
                data.append(line.strip())
            elif dim == 2:
                data.append(line.strip().split(','))
    return data

def _menu():
    print(""" 1 - search a 1D array
 2 - search a 2D array
 Q - quit
 """)
    while True:
        choice = input("Choice: ").strip().lower()
        if choice in ['1','2','q']:
            return choice
        else:
            print("Invalid choice. Try again")

# Data and functions
data = {'1': _openData("numberlist.txt"),
        '2': _openData("numbertable.csv",dim=2)}
search = {'1': linearSearch,
          '2': linearTableSearch}

# Test code
if __name__ == "__main__":
    while True:
        choice = _menu()
        if choice == 'q': break # Quit was chosen
        print("Press enter with no value when done")
        while True:
            item = input("Search for: ")
            if not item:
                break # No value entered - stop search
            if search[choice](item,data[choice]):
                print(f'Item {item} was found')
            else:
                print(f'Item {item} was NOT found')
    print("Finished")
