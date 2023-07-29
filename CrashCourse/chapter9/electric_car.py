from car2 import Car


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year, battery_size):
        """Initialize attributes of the parent class."""
        super().__init__(make,model,year)
        self.battery_size = battery_size
    
    # Define a new method for the child class
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size)  + "-kWh battery.")
    
    def fill_gas_tank(self):
        """Electric cars do not have gas tank"""
        print("This car does not require a gas tank!")

my_tesla = ElectricCar('Tesla', 'Model S', '2020',80)
print(my_tesla.get_descriptive())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()
