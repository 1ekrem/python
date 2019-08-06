class TestClass:
    'First Class is created: TestClass'
    pass

class Employee:
    'Common base class for all employees'

    empCount = 0 

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount +=1

    def displayCount(self):
        print("Total employee {}".format(Employee.empCount))

    def displayEmployee(self):
        print("Name:", self.name, "Salary:", self.salary)
    
emp1 = Employee("Ekrem", 135)
emp2 = Employee("Burhan", 125)

emp1.displayEmployee()
emp2.displayEmployee()
emp1.displayCount()

emp1.age = 7

print(emp1.age)

