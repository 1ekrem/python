#Create a class
class Employee:
    #Initialize the Employee class attribute
    def __init__(self, name, id):
        self.id = id
        self.name = name

    #Create a function to print the values in the class
    def display(self):
        print("Name: {1} \nID: {0}".format(self.id, self.name))

#Create an instant of the class
emp1 = Employee('Ekrem Ersayin', '07')
emp2 = Employee('Burhan Altintop', '11')

#Call the function from the class
emp1.display()
emp2.display()
