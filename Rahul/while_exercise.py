print("How far do you want to go. E.g. 50, 100, 500")
number = int(input())

print("By what number do you want to multiply with? E.g. 2,3,8,9")
multiplier = int(input())

print("What number would you like you begin with?")
count= int(input())


if count <= 0 :
    print("Do you want to enter a new number? yes or no")
answer = str(input())

if answer=="no":
    print("Good Bye, please terminate the code")
#Ask how to terminate the code here --->  break


if answer=="yes":
    print("Please enter the new number")
count = int(input())


while count<number:
    print (count)
    #count = count+1
    count = count * multiplier