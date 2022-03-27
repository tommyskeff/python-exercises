# Write a function called circlearea() that 
# takes a radius (float) as an argument, and 
# then returns the area of a circle of that 
# radius (also as a float).
  
import math

def circle_area(radius):
  return math.pi * (radius ** 2)

radius = float(input("Radius: "))
area = circle_area(radius)
print(f"Circle of radius {radius} has area {area}")