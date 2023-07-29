"""
9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of
the class will work; just pick the one you like better. Add an attribute called
flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand, and call this method.
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
    



class IceCreamStand(Restaurant):
    
    def __init__(self, restaurant_name, cuisine_type, flavors):
        self.flavors = flavors
        super().__init__(restaurant_name, cuisine_type)
        
    def iceCreamFlavors(self):
        self.flavors = ["Strawberry","Coconut","Pistachio"]
        
        print("We have the following flavors;")
        for flavor in self.flavors:
            print(flavor)

ice_shop = IceCreamStand("Darianin Yeri", "Russian", "Coconut")

ice_shop.describe_restaurant()

ice_shop.set_number_served(5)
ice_shop.describe_restaurant()

ice_shop.increment_number_served(18)
ice_shop.describe_restaurant()

ice_shop.iceCreamFlavors()



print("---------- NEW LINE --------")

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

"""
9-8. Privileges: Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges.
"""

class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges
        
    
    def show_privileges(self):
        print("The admin has the following privileges;")
        privileges = ["can add post", "can delete post", "can ban user"]
        for privilege in self.privileges:
            print(privilege)

"""
9-7. Admin: An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list
of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method.
"""

class Admin(User):
    def __init__(self, first_name, last_name, title, location, privileges):
        super().__init__(first_name, last_name, title, location)
        self.privileges = Privileges(privileges)

new_admin = Admin("Pupsik", "Papichulo", "Day Sleeper", "Brooklyn", "Set")

new_admin.privileges.show_privileges()


     
