import math 

def area(r):
    """'Area of a circle with radius 'r'."""
    return math.pi * (r**2)

radii = [2, 5 , 7.1, 0.3, 10]

# Method 1: Direct Method

areas = []
for r in radii:
    a = area(r)
    areas.append(a)

print(areas)

## Method 2 : Use 'map' function

print(list(map(area, radii)))

# Example - Let's converts tempetures to Fahrenheit
temps = [("Berlin", 29), ("Cairo", 36), ("Istanbul", 21), ("New York", 28), ("Tokyo", 27), 
("London", 22), ("Beijing", 32), ("Los Angeles", 26)]

c_to_f = lambda data: (data[0], (9/5)*data[1]+32)
print(list(map(c_to_f, temps)))