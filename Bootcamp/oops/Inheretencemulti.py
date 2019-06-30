
class Calculation1:
    def Summation(self, a, b):
        return a+b

class Calculation2:
    def Multiplication(self, a, b):
        return a*b

class Derived(Calculation1, Calculation2):
    def Divide(self,a,b):
        return a/b

d = Derived()

print(d.Summation(10,5))
print(d.Multiplication(10,5))
print(d.Divide(10,5))

#Check if it is a subclass
print("iS Subclass: ", issubclass(Derived, Calculation2))
print("iS Subclass: ", issubclass(Calculation1, Calculation2))
print("iS Subclass: ", issubclass(Derived, Calculation1))
print("iS instance: ", isinstance(d, Calculation2))
