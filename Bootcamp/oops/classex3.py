# Python Non-Parameterized Constructor Example

class Student:
    #Constructor - Non parameterized
    def __init__(self):
        print("This is non parameterized constructor")
    def show(self,name):
        print("Hello", name)

student = Student()
student.show("John")
