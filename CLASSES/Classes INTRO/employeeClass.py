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

if __name__ == "__main__":
    vm = Employee()
    vm.setName('Vital')
    vm.display()
    vm.setAge(38)
    vm.display()
    vm.age = 90
    vm.display()
    sd = Position()
    sd.display()