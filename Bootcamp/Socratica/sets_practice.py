"""
You can add different types of data to the set. 
Each value in sets are called element
Sets do not contain duplicate elements
To remove an element from the sets, use remove function or discard method.
    - Remove: If you try to remove an element that is not in the set by using Remove() - returns an error message
    - Remove: If you try to remove an element that is not in the set by using Discard() - Only returns what is currently contained in the set. 
"""
example = set()

example.add(42)
example.add(False)
example.add(3.14159)
example.add("Thorium")

print(example)

example.remove(42)
print(example)
example.discard("hi")
print(example)

example2 = set([20, True, 2.71828, "Helium"])
print(len(example2))
example2.clear()
print(example2)


# How to union the sets
odds = set([1, 3, 5, 7, 9])
evens = set([2, 4, 6, 8, 10])
prime = set([2, 3, 5, 7])
composites = set([4, 6 , 8, 9, 10])

print("Odds union even")
print(odds.union(evens))

print("Evens union odds")
print(evens.union(odds))

print("Odds")
print(odds)

print("Evens")
print(evens)

print("Odds intersection prime")
print(odds.intersection(prime))

print("Prime intersection even")
print(prime.intersection(evens))

print("Even intersection odds")
print(evens.intersection(odds))

print("Prime union composite")
print(prime.union(composites))

print("Test to see if an element in the set")
test = 2 in prime
print(test)