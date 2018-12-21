numbers = [5,4,0,2,7]

# min = numbers[0]
# for i in numbers:
#     if i < min:
#         min = i
# print(min)

min = numbers[0]
min2 = numbers[1]
for i in numbers:
    if i <= min:
        min = i
    elif i < min2:
        min2 = i
print(min)
print(min2)
