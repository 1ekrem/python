class Cat():
    """A simple attempt to model a dog."""
    
    def __init__(self, name, age):
        """Initialize name and age atributes."""
        self.name = name
        self.age = age
        
    def sit(self):
        """Simulate a cat sitting in response to a command."""
        print(self.name.title() + " is now sitting.")
    
    def roll(self):
        """Simulate a cat rolling in response to a command."""
        print(self.name.title() + " rolled over!")
        
my_cat = Cat("Pupsik",2)

print("My cat's name is " + my_cat.name.title() + ".")
print("My cat's age is " + str(my_cat.age)  + "." )

my_cat.roll()
my_cat.sit()