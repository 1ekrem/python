
#i=0 # initialize a value

# while i <= 6:
#     print("i is now {}".format(i))
#     i+=2

guessed_exit = ["south","norht east","south"]

chosen_exit=""

while chosen_exit not in guessed_exit:
    chosen_exit=input("Please enter a direction to exit: \n")
    if chosen_exit=="quit":
        print("Game Over!")
        break
print("Great! You have just exited the loop.")