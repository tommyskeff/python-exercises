# Throwing two dice generates a random integer between 2 and 12.
# Edit the code to use the random module and generate 50 random integers between 2 and 12 inclusive.
# Print the integer on the same line with a space between each one (eg 2 5 10 7 2 ...)
# Follow the instructions in the comments closely.

DICE_COUNT = 2
DICE_SIDES = 6
THROWS = 50

import random

print(" ".join([str(sum([random.randint(1, DICE_SIDES) for _ in range(DICE_COUNT)])) for _ in range(THROWS)]))