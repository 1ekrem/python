# Range between 0 to 10 but print only number //2=0
for i in range(0,10, 4):
    print("i is {} ".format(i))
print("==========")

for k in range (1,5):
    for j in range(1,5):
        print("{1} times {0} is {2}".format(k,j,k*j))
    print("===============")