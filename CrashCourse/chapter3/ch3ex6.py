# 3-6. More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
# statement to the end of your program informing people that you found a
# bigger dinner table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.

invitees = ["Elon Musk", "Nikola Tesla", "Albert Einstein"]
print(invitees)
print("-"*25)

invitees.insert(0, "Ekrem Ersayin")
invitees.insert(3,"Daria Vizniuk")
invitees.append("Bulent")

for invitee in invitees:
    print(invitee + ", Please come and eat")
    
