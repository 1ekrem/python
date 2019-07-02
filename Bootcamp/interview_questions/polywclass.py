'''
Polymorphism with class methods. 
'''

class Turkey():
    def capital(self):
        print("Ankara is the capital of Turkey")
    def language(self):
        print("Turkish is the primary language of Turkey")
    def type(self):
        print("Turkey is an emerging market")

class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA")
    def language(self):
        print("English is the primary language of USA")
    def type(self):
        print("USA is the market leader")

obj_tur=Turkey()
obj_usa=USA()

for country in (obj_tur, obj_usa):
    country.capital()
    country.language()
    country.type()