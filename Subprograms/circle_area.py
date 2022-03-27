import math


def circlearea(radius):
    return math.pi * (radius ** 2)


radius = float(input("Radius: "))
area = circlearea(radius)
print(f"Circle of radius {radius} has area {area:.1f}")
