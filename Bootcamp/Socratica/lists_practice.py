"""
Lists make it easier to work with data.
Lists are built-in data structure for stroing and accessing objects which belong in a specific sequence.
"""

# Two ways to create lists

example = list()
example = []

prime = [2, 3, 5, 7, 11, 13]

#Note: In SETS order is not important, yet in LISTS, order is everything.

prime.append(17)
prime.append(19)

print(prime)
print(prime[0])
print(prime[1])
print(prime[-1])


#Slicing
print(prime[2:5])
print(prime[0:6])

example2 = [128, True, "Alpha", 1.732, [64, False]]
#Note: Many languages require lists to contain values of the same type but not Python. 
# With python, you are free to insert multiple data types in the same list.
# Lists can also contain duplicate value.

rolls = [4, 7, 2, 7, 9]
print(rolls)

# Combining LISTS are called CONCATENATION.

numbers = [1, 2, 3]
letter = ['a', 'b', 'c', 'a', 's', 'a']
combined = numbers + letter
print(combined)

print(letter.count('a'))
r = numbers.reverse()
print(r)