class Animal:
    def speak(self):
        print("Speaking")

class Dog(Animal):
    def speak(self):
        print("Barking")
        

obj = Dog()
obj.speak()