#message = input("Tell Me somethin, and I will repeat it back to you: ")
#
#print(message)

print("-"*25,'NEW LINE','-'*25)

# You can store your prompt in a variable and pass that variable to the input() function.
# += is multi-line string. 
# prompt = "If you tell us who you are,  we can personalize the messages you see."
# prompt += "\nWhat is your first name?"

age = int(input("How old are you?"))

if age > 18:
    print("You are allowed to vote!")
else:
    print("Sorry! See you next time") 