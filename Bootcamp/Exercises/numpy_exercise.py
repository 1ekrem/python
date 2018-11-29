import numpy as np

a = np.array([(8,9,10),(11,12,13)])
print(a)

print("*"*50)

b=a.reshape(3,2)
print(b)

print("*"*50)

c = a.reshape(2,3)
print(c)

print("*"*50)

print(a.shape)
print(a.size)
print(a.itemsize)

# array_1 = [0,1,2,3,4]
# array_2 = [5,6,7,8,9]

# np.
