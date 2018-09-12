#Dictionaries are unordered items that contain key and value combinations.

fruit= {"orange": " a sweet, orange-yellowish citrus fruit",
"apple": "good for making cider",
"lemon": "a sour, yellow citrus fruit",
"grape": "a small, sweet fruit growing on tree in bunches"
}

print(fruit)

print("="*50)

print(fruit["lemon"])

print("="*50)

for key, value in fruit.items():
    print(key, ": ",value)

#how to add a value to dictionary

fruit["pear"]="an odd shaped apple"
print("="*50)
for key, value in fruit.items():
    if key=="pear":
        print("Just added: {} to the dictionary. \nThe value is: {}".format(key,value))
    

#How to override a recently added value to the dictionary.
fruit["pear"]="light green looking odd shaped apple"

print("="*50)
for key, value in fruit.items():
    if key=="pear":
        print("Just added: {} to the dictionary. \nThe updated value is: {}".format(key,value))

#how to remove a key&value combination from the dictionary.

del fruit["apple"]

print("="*50)
for key, value in fruit.items():
    if key=="apple":
        print("{} is still in the dictionary. \nThe value is: {}".format(key,value))
print("Apple is not in the dictionary anymore.")

print("="*50)
print("Keys in the dictionary are as following: ")
for key, value in fruit.items():
    print(key)

print("="*50)
while True:
    dict_key = input("Please enter a fruit name: ")
    if dict_key =="quit":
        break
    if dict_key in fruit:
        description = fruit.get(dict_key)
        #description = fruit.get(dict_key, "We dont have a "+dict_key)
        print(description)
    else:
        print("We don't have a "+dict_key)