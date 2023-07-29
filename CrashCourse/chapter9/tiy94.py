"""
9-4. Number Served: Start with your program from Exercise 9-1 (page 166).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number
of customers that have been served. Call this method with a new number and
print the value again.
Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any number
you like that could represent how many customers were served in, say, a
day of business.
"""
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print("Name of the restaurant is " + self.restaurant_name)
        print("Cuisine Type of the resturant is " + self.cuisine_type)
        print("Total number of reservations for tonight: " + str(self.number_served))
    
    def open_restaurant(self):
        print("The restaurant is open. Please make your reservation!")
    
    def set_number_served(self, numberServed):
        self.number_served = numberServed
                
    def increment_number_served(self, incNumber):
        self.number_served += incNumber
    

MyRestaurant = Restaurant("Ekremin Yeri", "Turkish")

MyRestaurant.describe_restaurant()
MyRestaurant.open_restaurant()

MyRestaurant.set_number_served(50)
MyRestaurant.describe_restaurant()

MyRestaurant.increment_number_served(100)
MyRestaurant.describe_restaurant()

MyRestaurant.increment_number_served(20)
MyRestaurant.describe_restaurant()
"""
9-5. Login Attempts: Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 166). Write a method called increment_
login_attempts() that increments the value of login_attempts by 1. 

Write another method called reset_login_attempts() that resets the value of login_
attempts to 0.

Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0.
"""

class User():
    def __init__(self, first_name, last_name, title, location):
        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.location = location
        self.login_attempts = 0
    
    def describe_user(self):
        print("The user's first and last name is " + self.first_name + " " + self.last_name)
        print(self.first_name + " is from " + self.location + " and his/her title is " + self.title)
        if self.login_attempts == 0:
            print("Number of Login Attemps: " + str(self.login_attempts))
        
    def greet_user(self):
        print("Hello " + self.first_name + "! Thank you for your time!")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
        print("Number of Login Attemps: " + str(self.login_attempts))
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        print("Login Attempts have been reset. \nCurrent Attempt Number: " + str(self.login_attempts))

user1 = User("Ekrem", "Ersayin", "Trader", "NYC")
print("\n--------- NEW LINE ---------")
user1.describe_user()
user1.greet_user()
user1.increment_login_attempts()
user1.reset_login_attempts()
user1.describe_user()

