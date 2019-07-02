print("All Numbers")

print ("Enter what number you want to start the chart")
range1=int(input())
print ("Enter what number you want to end the chart")
range2=int(input())
range3=range1
range4=range2

for k in range(range1,range2+1):
    print()
    for j in range(range3,range4):
        print(k*j, end='')