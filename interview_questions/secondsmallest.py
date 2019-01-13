numbers = [5,4,2,7]

min1 = numbers[0]
min2 = numbers[1]

for i in numbers:
    if i < min1:
        min1 = i
    elif i < min2:
        min2 = i

print(min1)
print(min2)

