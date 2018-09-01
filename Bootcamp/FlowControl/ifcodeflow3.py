



print("Please guess a number between 1 and 10")

guess=int(input())

if guess !=5:
    if guess <5:
        print("Please guess higher.")
    else:
        print("Please guess lower.")

    guess=int(input())
    if guess==5:
        print("Well done! You guessed it!")
    else:
        print("Sorry, you have not guessed correctly!")
else:
    print("You got it first time! ")