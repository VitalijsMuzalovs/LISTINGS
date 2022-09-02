class Employee:
    def __init__(self) -> None:
        self.age = None

    def setName(self,name):
        self.name = name

    def setAge(self,value):
        self.age = value

    def display(self):
        print("Ņame:",self.name,'Age:',self.age)

class Position(Employee):
    def __init__(self):
        self.position = "undefined"
    
    def setPosition(self,position):
        self.position = position
    
    def display(self):
        print("Position:",self.position)

