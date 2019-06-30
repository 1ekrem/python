class Employee:
    __count = 0

    def __init__(self, fname, lname, age):
        Employee.__count = Employee.__count +1
        self.fname = fname
        self.lname = lname
        self.age = age
    
    def display(self):
        print("The number of employees", Employee.__count)
        print(self.fname, self.lname, self.age)

emp1 = Employee('Ekrem', 'Ersayin', '29')
emp2 = Employee('Burhan', 'Altintop', '35')

print(emp1.display())
print(emp2.display())