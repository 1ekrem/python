print("Mathematical Chart")


print ("At what number of row would you like to begin your chart?")
range1=int(input())
print ("At what number of row would you like to end your chart?")
range2=int(input())
print ("Which column of the chart would you like to see?")
range3=int(input())

range4=range3+1

for k in range(range1,range2+1):
    print()
    for j in range(range3,range4):
        print(k*j, end='')