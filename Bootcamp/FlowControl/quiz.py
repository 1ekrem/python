# value = 8
# answer = 0

# for x in range(1, 13):
#     answer = value * x
#     print("{0} times {1} is {2}".format(x, value, answer))


for p in range(30):
    if p % 3==0 or p % 5==0:
        continue
    print(p)
print("=====================")
for x in range(30):
    if x % 3!=0 and x % 5!=0:
        print(x)
print("=====================")
# for y in range(30):
#     if y % 3!=0 or y % 5!=0:
#         print(y)        