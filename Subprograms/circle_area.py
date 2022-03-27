import math


def circle_area(radius):
    return math.pi * (radius ** 2)


radius = float(input("Radius: "))
area = circle_area(radius)
print(f"Circle of radius {radius} has area {area:.1f}")
