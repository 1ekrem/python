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

#B

c = Car()

c.start()
c.drive()
c.stop()

print("")

b = BMW()

b.start()
b.stop()