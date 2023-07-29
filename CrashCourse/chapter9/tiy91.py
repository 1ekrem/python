"""
9-1. Restaurant: Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indicating
that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes
individually, and then call both methods.
"""

class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print("Name of the restaurant is " + self.restaurant_name)
        print("Cuisine Type of the resturant is " + self.cuisine_type)
    
    def open_restaurant(self):
        print("The restaurant is open. Please make your reservation!")
        
my_rest1 = Restaurant("De Le Ekrem", "Turkish")

print(my_rest1.restaurant_name.title())
print(my_rest1.cuisine_type)
my_rest1.describe_restaurant()
my_rest1.open_restaurant()

"""
9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance.
"""
print("\n")
my_rest2 = Restaurant("Nusret", "Turkish")
my_rest3 = Restaurant("Bold Guys", "American")
my_rest4 = Restaurant("La Meat", "French")

my_rest2.describe_restaurant()
my_rest3.describe_restaurant()
my_rest4.describe_restaurant()

"""
9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user
"""

class User():
    def __init__(self, first_name, last_name, title, location):
        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.location = location
    
    def describe_user(self):
        print("The user's first and last name is " + self.first_name + " " + self.last_name)
        print(self.first_name + " is from " + self.location + " and his/her title is " + self.title)
        
    def greet_user(self):
        print("Hello " + self.first_name + "! Thank you for your time!")

user1 = User("Ekrem", "Ersayin", "Trader", "NYC")
user2 = User("Ozgur", "Ersayin", "Sales Person", "Istanbul")
user3 = User("Pupsik", "Ersayin", "Sleeper", "Mexico")

print("\n")
user1.describe_user()
user1.greet_user()

print("\n")
user2.describe_user()
user2.greet_user()

print("\n")
user3.describe_user()
user3.greet_user()
