# Use the random module to print out 5 random 
#   numbers between 0 and 1.
# Print each random number out on its own line.
# Follow the instructions in the comments closely.

BOUNDS = 0, 1
NUMBERS = 5

import random

print("\n".join([str(random.randint(BOUNDS[0], BOUNDS[1])) for _ in range(NUMBERS)]))