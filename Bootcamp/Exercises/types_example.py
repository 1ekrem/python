fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]

fruits.update(more_fruits)
print(fruits)

#fruits.remove("banana")
#print(fruits)

fruits.discard("banana")
print(fruits)

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(car.get("model"))
print(car["model"])

print(car)
car["year"]=2018
print(car)

car["color"]="red"
print(car)

car.pop("model")
print(car)

car.clear()
print(car)
