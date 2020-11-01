# Consider a list of newly registered but unverified users of a website. After
# we verify these users, how can we move them to a separate list of confirmed users?

unconfirmedUsers = ['pupsik','papi','chulo']
confirmedUsers = []
blockedUser = []

while unconfirmedUsers:
    confirmedUsers = unconfirmedUsers.pop()
    for user in confirmedUsers:
        if user == 'chulo':
            blockedUser = user
        else:
            pass

    print("Confirmed User: {}".format(confirmedUsers))
    
print("--------------- NEW LINE --------------")

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)