"""
8-12. Sandwiches: Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the sandwich
that is being ordered. Call the function three times, using a different number
of arguments each time.
"""

def make_sandwich(*items):
    for item in items:
        print("- " + item)

make_sandwich("cheese","tomato","olive\n")
make_sandwich("cheese","tomato","olive","parsley\n")
make_sandwich("cheese","tomato","olive","parsley", "spinach\n")

"""
8-13. User Profile: Start with a copy of user_profile.py from page 153. Build
a profile of yourself by calling build_profile(), using your first and last names
and three other key-value pairs that describe you.
"""

def build_profile(first, last, **trader_info):
    trader_profile = {}
    trader_profile['First Name'] = first
    trader_profile['Last Name'] = last
    
    for key, value in trader_info.items():
        trader_profile[key] = value
    return trader_profile
    #print(trader_profile)

trader_1 = build_profile("Ekrem", "Ersayin", 
                            Title="Head of Trading", 
                            Office= "NYC - Midtown")
print(trader_1)
    

"""
8-14. Cars: Write a function that stores information about a car in a dictionary.
The function should always receive a manufacturer and a model name. It
should then accept an arbitrary number of keyword arguments. Call the function
with the required information and two other name-value pairs, such as a
color or an optional feature. Your function should work for a call like this one:
car = make_car('subaru', 'outback', color='blue', tow_package=True)
Print the dictionary that’s returned to make sure all the information was
stored correctly.
"""

def car_finder(make, model, **features):
    car_profile = {}
    car_profile["Manufacturer"] = make
    car_profile["Model"] = model
    
    for key, val in features.items():
        car_profile[key] = val
    return car_profile
    
first_car = car_finder("Lexus", "IS250 Fsport", color="Pearl Grey", tow_package="AWD")
print(first_car)

test_car = car_finder('subaru', 'outback', color='blue', tow_package=True)
print(test_car)
