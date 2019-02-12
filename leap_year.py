import random

def leapyear():
    n = int(input("Enter year: "))
    if n%4==0 and (n%400==0 or not n%100==0):
        print("{} is a leap year!".format(n))
    else:
        print("{} is NOT leap year!".format(n))

def multiplicationGame():
    x1=random.randint(1,10)
    x2=random.randint(1,10)

    input("Press enter to see the numbers: ")
    print("First Number: ",x1, " Second Number: ",x2 )
    guess = int(input("What's the multiplication of the two numbers shown?: "))

    if guess==(x1*x2):
        print("Congratulations! Multiplication is {}".format(x1*x2))
    else:
        print("Try later again!")

# leapyear()
multiplicationGame()