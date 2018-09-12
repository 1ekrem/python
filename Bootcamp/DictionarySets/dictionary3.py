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

print(fruit)

ordered_keys = sorted(list(fruit.keys()))

for f in ordered_keys:
    print(f+" - "+fruit[f])

