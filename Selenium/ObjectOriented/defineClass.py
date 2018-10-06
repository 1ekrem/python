"""
Object Oriented Programming
"""

class Car(object): #Common way to start with CAPITAL letter. 

    wheels = 4 #every car has 4 wheels
    #Car class inherits the object class which is included in python.

    def __init__(self, make, model): #This is used to initialize all the attributes of an object.
        self.make = make # Define attributes of the classes
        self.model = model
        #Self is always the first parameter used in python

    def info(self):
        print("Make of the car: " + self.make)
        print("Model of the car: " + self.model)

print(Car.wheels)

c1 = Car('BMW', '325i') #Create instance
print('C1 wheel', c1.wheels)
c1.wheels = 3
print('C1 wheel update:', c1.wheels)
# c1.info()

c2 = Car('Mercedes', 'C300')
c2.info()

c3 = Car('Honda', 'Accord')
c3.info()