#Counting the number of objects of a class
class Student:
    count = 0

    def __init__(self):
        Student.count = Student.count +1
s1 = Student()
s2 = Student()
s3 = Student()
print("The number of student:", Student.count)