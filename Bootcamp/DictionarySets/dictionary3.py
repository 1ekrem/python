fruit= {"orange": " a sweet, orange-yellowish citrus fruit",
"apple": "good for making cider",
"lemon": "a sour, yellow citrus fruit",
"grape": "a small, sweet fruit growing on tree in bunches",
"lime": "a sour, green citrus fruit"
}

# for i in range(10):
#     for snack in fruit:
#         print(snack +" is "+ fruit[snack])
#     print("-"*50)

# print(fruit)

# ordered_keys = sorted(list(fruit.keys()))

# for f in ordered_keys:
#     print(f+" - "+fruit[f])

# print(fruit.keys())
# print(fruit.values())

fruit["tomato"]="round shaped, red juicy fruit."

# for a,b in fruit.items():
#     if b.__contains__("red"):
#         print(a,b)

# Convert the dictionary into tuple
f_tuple=tuple(fruit.items())
print(f_tuple)

print("="*40)

for snack in f_tuple:
    item, description=snack
    print(item + " is " + description)