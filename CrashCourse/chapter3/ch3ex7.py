# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and you have space for only two guests.
# • Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.
#Done
# • Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print
# a message to that person letting them know you’re sorry you can’t invite
# them to dinner.
#
# • Print a message to each of the two people still on your list, letting them
# know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end
# of your program.


invitees = ["Elon Musk", "Nikola Tesla", "Albert Einstein"]
print(invitees)
print("-"*25)

invitees.insert(0, "Ekrem Ersayin")
invitees.insert(3,"Daria Vizniuk")
invitees.append("Bulent")

for invitee in invitees:
    print(invitee + ", Please come and eat")

print("\n" + "There will be only 2 people invited")

invitees.pop()
print(invitees)

invitees.pop()
print(invitees)

invitees.pop()
print(invitees)
invitees.pop()
print(invitees)

print("Dear" , invitees[0].title() , "and" ,  invitees[1].title() , "you are still invited" )

del invitees[1]
del invitees[0]

print(invitees)
