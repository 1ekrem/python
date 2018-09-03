for i in range(1,10):
    print(i,"-","Ekrem") 

print(" ")
print("Mathematical Chart")

# print ("Enter what number you want to start the chart")
# range1=int(input())
# print ("Enter what number you want to end the chart")
# range2=int(input())
# range1=range3
# range2=range4

print ("At what number of row would you like to begin your chart?")
range1=int(input())
print ("At what number of row would you like to end your chart?")
range2=int(input())
print ("What number of the chart would you like to see?")
range3=int(input())

range4= range3+1

for k in range(range1,range2+1):
    print()
    for j in range(range3,range4):
        print(k*j, end='')


