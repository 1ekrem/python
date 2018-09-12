fruit= {"orange": " a sweet, orange-yellowish citrus fruit",
"apple": "good for making cider",
"lemon": "a sour, yellow citrus fruit",
"grape": "a small, sweet fruit growing on tree in bunches"
}

veg= {"onion": " Great on the grill",
"sprouts": "mmm lovely",
"spinach": "Best food I like to eat",
}

# veg.update(fruit)

# print("="*40)
# print("Updated Veg Dict")
# print(veg)
# print("="*40)


#Let's copy the dictionary

nice_and_nasty = fruit.copy()
nice_and_nasty.update(veg)

print("Nice and Nast Dict")
print(nice_and_nasty)
print("="*40)
print("Vegs Dict")
print(veg)
print("="*40)
print("Fruits Dict")
print(fruit)