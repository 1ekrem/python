import requests

class Employee:

    raise_ratio = 1.05

    def __init__(self, fname, lname, pay):
        self.fname = fname
        self.lname = lname
        self.pay = pay

    @property
    def email(self):
        return '{}{}@email.com'.format(self.fname, self.lname)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)
    
    def apply_raise(self):
        self.pay = (self.pay * self.raise_ratio)
