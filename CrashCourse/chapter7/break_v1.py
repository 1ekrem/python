# Using break to stop the loop

prompt = "\nPlease enter the name of a city you have visited: "

while True:
    cityName = input(prompt).upper()
    # Logic to break
    if cityName == 'NYC':
        print("{} is in the HEART!".format(cityName))
        break
    else:
        print("{} is on Earth!".format(cityName))
        

# Infinite Loop

x = 1
while x < 2:
    print(x)
    #Finite the loop by conditioning
    if x == 1:
        break 