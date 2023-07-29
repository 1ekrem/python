"""
If you dont know how many arguments you will need in the function then  
"""

def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
    
    
make_pizza("Tomato")
make_pizza("Mushroom", "Tomato", "Olive")

def make_pizza_size(size, *toppings):
    """Print the list of toppings that have been requested."""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza_size(15, "Mushroom", "Tomato", "Olive")


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile("Ekrem", "Ersayin",
                             Location = 'NYC',
                             Title = 'Head of Trading')

print(user_profile)