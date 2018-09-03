a=12
b=3

print("a:",a,"b:",b)
print("a+b->",a+b)
print("a-b->",a-b)
print("a*b->",a*b)
print("a/b->",a/b) # Returns float value
print("a//b->",a//b) # Return integer value
print("a%b->",a%b) #Remainder

for i in range(1,a/b): 
# The script should fail becasue a/b will return float which should be an integer.
# To get an integer value, USE a//b. 
    print(i)

