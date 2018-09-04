print("Please guess a number between 1 and 10")

guess=int(input())

if guess <5:
    print("Please guess higher")
    guess=int(input())
    if guess==5:
        print("Well done! You guessed it!")
    else:
        print("Sorry, you have not guessed correctly!")
elif guess > 5:
    print("Please guess lower")
    guess=int(input())
    if guess ==5:
        print("Well done! You guessed correctly!")
    else:
        print("Sorry, you have not guessed correctly!")
else:
    print("You got it first time! ")