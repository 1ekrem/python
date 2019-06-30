#Inheretence

class Animal:
    def speak(self):
        print("Animal Speaking")

#Child class Dog inherits the base class Animal 
class Dog(Animal):
    def bark(self):
        print("Dog barking")

d = Dog()
d.speak()
d.bark()