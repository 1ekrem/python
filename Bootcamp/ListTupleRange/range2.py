decimals = range(0,100)
print(decimals)

my_range = decimals[3:40:3]
print(my_range)

for i in my_range:
    print(i)

print("="*40)

print("Confirm if the ranges are the same: ",my_range==range(3,40,3))

print("="*40)

x=range(0,100)[::-5]
y=range(99,0,-5)

print(x)
print(y)
print(x==y)

for i in x:
    print(i)

print("="*40)

for k in y:
    print(k)