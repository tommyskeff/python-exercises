import random

DICE_COUNT = 2
DICE_SIDES = 6
THROWS = 50

print(" ".join([str(sum([random.randint(1, DICE_SIDES) for _ in range(DICE_COUNT)])) for _ in range(THROWS)]))
