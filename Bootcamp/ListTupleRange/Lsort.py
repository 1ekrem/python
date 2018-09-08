odd = [1,3,5,7,9]
even = [2,4,6,8]

number = even+odd
print(number)

numbers_in_order=sorted(number)
print(number)
if number==numbers_in_order:
    print("The lists are equal")
else:
    print("The lists are not equal")

if numbers_in_order==sorted(number):
    print("The lists are equal")
else:
    print("The lists are not equal")

number.append(11)
print(number)

number.append(0)
print(number)

number.sort()
print(number)

number.reverse()
print(number)

number.insert(4, 12) # 4th index, object is '12'
print(number)

number.sort()
print(number)

