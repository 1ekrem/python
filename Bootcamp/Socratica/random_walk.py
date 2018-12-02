import random

def random_walk(n):
    """Return coordinates after 'n' block random walk."""
    x=0
    y=0
    for i in range(n):
        step = random.choice(['N','S','E','W'])
        if step == 'N':
            y = y + 1
        elif step == 'S':
            y = y - 1
        elif step == 'E':
            x = x + 1
        else:
            x = x - 1
    return(x,y)
    
# for i in range(25):
#     walk = random_walk(10)
#     print(walk, "Distance from home = ", abs(walk[0]) + abs(walk[1]))

# Question: What is the longest random walk you can take -->
# so that on average you will end up 4 blocks or fewer from home?
# In other words, there is less than a 50% chance you pay for transportation
# number_of_walks = 1000
# for walk_lenght in range (1, 31):
#     no_transport = 0
#     for i in range(number_of_walks):
#         (x,y) = random_walk(walk_lenght)
#         distance = abs(x) + abs(y)
#         if distance <= 4:
#             no_transport += 1
#     no_transport_percentage = float(no_transport)/number_of_walks
#     print("Walk size = ", walk_lenght, " / % of no transport = ", 100*no_transport_percentage)

# Challenge
# Find the longest random walk which will, on average, leave you less than 5 bloscks from home.
# So distance should be as -> distance < 5

number_of_walks = 10000
for walk_lenght in range (1, 31):
    no_transport = 0
    for i in range(number_of_walks):
        (x,y) = random_walk(walk_lenght)
        distance = abs(x) + abs(y)
        if distance < 5:
            no_transport += 1
    no_transport_percentage = float(no_transport)/number_of_walks
    print("Walk size = ", walk_lenght, " / % of no transport = ", 100*no_transport_percentage)
