class BankofA:
    def getROI(self):
        return 10

class Morgan(BankofA):
    def getROI(self):
        return 7
    
class Goldman(BankofA):
    def getROI(self):
        return 8

b1 = BankofA()
b2 = Morgan()
b3 = Goldman()

print("The rate of Bank of America:", b1.getROI())
print("The rate of Morgan:", b2.getROI())
print("The rate of Goldman:", b3.getROI())