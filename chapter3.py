import math
#import numpy as np
"""
#ex1


def my_sinh(x):
    sinh_value = (math.exp(x) - math.exp(-x)) / 2
    return sinh_value
x = 0
y = my_sinh(x)
print(y)

x = 1
y = my_sinh(x)
print(y)

x = 2
y = my_sinh(x)
print(y)

#ex2

def my_checker_board(n):
    checkerboard = []
    for i in range(n):
        row = []
        for j in range(n):
            if (i + j) % 2 == 0:   #to know if the row is 1 or 0 by even or odd
                row.append(1)
            else:
                row.append(0)
        checkerboard.append(row)
        
    return checkerboard
n=1
print(my_checker_board(n))
n=2
print(my_checker_board(n))
n=3
print(my_checker_board(n))
n=5
print(my_checker_board(n))

#ex3

def my_triangle(b, h):
    area = 0.5 * b * h  #
    return area


base = 1
height = 1
area_of_triangle = my_triangle(base, height)
print("the area is {area_of_triangle}")

base = 2
height = 1
area_of_triangle = my_triangle(base, height)
print("the area is {area_of_triangle}")

base = 12
height = 5
area_of_triangle = my_triangle(base, height)
print("the area is {area_of_triangle}")

#ex4
import math

def my_cylinder(r, h):
  
    surface_area = 2 * math.pi * r**2 + 2 * math.pi * r * h
    volume = math.pi * r**2 * h
    
    return [surface_area, volume]


radius = 1
height =5
result = my_cylinder(radius, height)
print("{result[1]}")
"""

#ex5

