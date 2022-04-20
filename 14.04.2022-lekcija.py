##### CLASSES #####

# Class 1
"""
class Papagailis:
    suga = "putns"

    def __init__(self,name,age):
        self.name = name
        self.age = age

bl=Papagailis("zils",10)
wo=Papagailis("wooo",5)

print(f"BL ir {bl.__class__.suga}")
print(f"WO ir {wo.__class__.suga}")

print(f"{bl.name} ir {bl.age} gadu sens")
print(f"{wo.name} ir {wo.age} gadu sens")
"""
#========================================
# Child -> parent
"""
# PARENT
class Putns:
    def __init__(self):
        print("Putns ir gatavs!")
    def kas(self):
        print("Putniņš")
    def peld(self):
        print("Peld ātri")

# CHILD
class Pingvins(Putns):
    def __init__(self):
        print("Pingvins ir gatavs!")
    def kas(self):
        print("Pingvins")
    def skrien(self):
        print("Skrien ātri")

poga=Pingvins()
poga.kas()
poga.peld()
poga.skrien()
"""

### INCAPSULATING
"""
class Dators:
    def __init__(self):
        self._maxprice = 900
    def pardot(self):
        print(f"Sell price is: {self._maxprice}")
    def setMaxPrice(self,price):
        self._maxprice=price

c=Dators()
c.pardot()

c._maxprice=1000
c.pardot()

c.setMaxPrice(1111)
c.pardot()
"""

### POLYMORPHISM
#  ???