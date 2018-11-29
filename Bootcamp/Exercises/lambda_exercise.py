"""
lambda expression are nameless functions
"""
# x = lambda a : a + 10
# print(x(5))

# y = lambda a,b : a*b
# print(y(3,3))

# z = lambda a,b : a**b
# print(z(3,3))

# print('----Function----')
# def myfunca(n):
#     return lambda a : a*n

# m = myfunca(2)
# print(m(5))

print("----------Lambda Function----------")
def f(x):
    return 3*x +1

print(f(2))

g = lambda x: 3*x +1
print(g(2))

print("----------Lambda Function for String Manipulation----------")
full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print(full_name("    ekrem", "ERSAYIN"))

print("----------Lambda Function to sort list of strings----------")
# A function with no name: Create a expression, sort with lambda expression
scifi_authors = ["Isaac Asimov", "Ray Bradbury", "Robert Heinlein", "Arthus C. Clarke", 
"Frank Herbert", "Orson Scott Card", "Douglas Adams", "H. G. Wells", "Leigh Brackett"]

# help(scifi_authors.sort)
print(sorted(scifi_authors, key=lambda name: name.split(" ")[-1].lower()))

print("----------Lambda Function for mathematical calculations----------")
def build_quadratic_function(a, b, c):
    """Returns the function f(x) = ax^2 +bx +c"""
    return lambda x : a*x**2 + b*x + c

f = build_quadratic_function(2, 3, -5)
print(f(0))
print(f(1))
print(f(2))
print(f(5))
print(f(-1))
print("without creating an object/name -->", build_quadratic_function(3, 0 , 1)(2))