import random

BOUNDS = 0, 1
NUMBERS = 5

print("\n".join([str(random.randint(BOUNDS[0], BOUNDS[1])) for _ in range(NUMBERS)]))
