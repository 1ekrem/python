"""
Let’s write a new class representing a car. Our class will store information
about the kind of car we’re working with, and it will have a method that
summarizes this information:
"""
class Car():
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive(self):
        """Return a neatly formatted descriptive name"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def readOdometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    def updateOdometer(self, mileage):
        "Set the odometer reading to the given value"
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
        print("The odometer has gone up by " + str(miles))
    
    def fill_gas_tank(self, mileage):
        print( str(mileage) + " miles range left. Please fill gass.")

myNewCar = Car("Lexus", "IS250", "2014")

#print(myNewCar.get_descriptive())
#myNewCar.readOdometer()
#myNewCar.fill_gas_tank(18)
#
#myNewCar.updateOdometer(83500)
#myNewCar.readOdometer()
#
#myNewCar.updateOdometer(1000)
#myNewCar.readOdometer()
#
#myNewCar.increment_odometer(1000)
#myNewCar.readOdometer()

