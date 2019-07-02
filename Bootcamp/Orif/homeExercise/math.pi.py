import math
##print(dir(math))

#print(math.pi)

def volume(r):
    """Returns the volume of a sphere with radius r.""" # Doc-String - documents the information of the function

    v = (4.0/3.0) * math.pi * r**3
    print(v)

def triangle_area(b, h):
    """Returns the area of a triangle with base b and height h."""
    t_area= (0.5 * b * h)
    print(t_area) # Why 'return' doesn't return anything

triangle_area(3,6)