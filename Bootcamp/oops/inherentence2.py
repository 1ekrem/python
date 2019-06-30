#Inheretence

class Animal:
    def speak(self):
        print("Animal Speaking")

#Child class Dog inherits the base class Animal 
class Dog(Animal):
    def bark(self):
        print("Dog barking")

#Another Child of Animal inherits
class DogChild(Dog):
    def eat(self):
        print("Eating breed...")

d=DogChild()
d.speak()
d.bark()
d.eat()

