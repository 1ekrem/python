from car2 import Car

class Battery():
    """A simple attemp to model a battery for an electric car."""
    def __init__(self, battery_size):
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size)  + "-kWh battery.")
        
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        elif self.battery_size > 85:
            range = 'infinite'

        
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        if self.battery_size > 85:
            message_alt = ' Bullshit as NIKOLA :)'
            message += message_alt
        print(message)



class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year, battery_size):
        """Initialize attributes of the parent class."""
        super().__init__(make,model,year)
        self.battery = Battery(battery_size)
    
    
    def fill_gas_tank(self):
        """Electric cars do not have gas tank"""
        print("This car does not require a gas tank!")

my_tesla = ElectricCar('Tesla', 'Model S', '2020',86)
print(my_tesla.get_descriptive())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
