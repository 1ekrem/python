

number = int(input("Please enter a number: "))

while True:
    if number%2!=0:
        print("Odd: ",number)
    else:
        print("Even: ",number)
    break

#Continue until the negative number is entered
while True:
    number1 = int(input("Please enter a number"))
    if (number1 == -1 ):
        print("Terminated due to a negative number")
        break