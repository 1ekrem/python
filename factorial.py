print("Factorials")

print("Enter a number to calcualate the factorial")
number=int(input())

if number==0:
    x=1
else:
    x=1
    for i in range(1, number+1):
        x=x*i    
    print("The factorial number of ",number,"is ",x)

    