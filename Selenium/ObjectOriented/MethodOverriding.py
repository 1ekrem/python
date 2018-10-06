# What if I want to modify drive function so I want to use a new one.


class Car(object):

    def __init__(self):
        print("You just created the car instance")
    
    def start(self):
        print("Car is being started")
    
    def drive(self):
        print("Car is being driven")

    def stop(self):
        print("Car is being stopped")


class BMW(Car):

    def __init__(self):
        Car.__init__(self)
        print("You just created the BMW instance")

    def drive(self):
        super.drive() #'Super' keyword calls the main drive function from the main class. 
                #Car class is the main class, BMW is the child class. 
        print("This method has been overriden! You are driving a BMW, Enjoy...")
    
    def headup_display(self):
        print("This is a unique feature")

c = Car()

c.start()
c.drive()
c.stop()

print("")

b = BMW()

b.start()
b.drive()
b.stop()
b.headup_display()