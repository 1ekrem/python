#Parameterized Constructor Example

class Student:
    #Constructure - parameterized
    def __init__(self,name):
        print("This is parameterized constructor")
        self.name = name
    
    def show(self):
        print("Hello", self.name)

student = Student("John")
student.show()

