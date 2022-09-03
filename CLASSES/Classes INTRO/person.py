from classtools import AttrDisplay

class Person(AttrDisplay):
    def __init__(self,name,job=None,pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    
    def getSurname(self):
        return self.name.split()[-1]
    
    def giveRaise(self,percent):
        self.pay = round(self.pay * (1 + percent),2)

    # def __str__(self):
    #     return  f'[Person: {self.name} \tPay: {self.pay}]'

class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self,name,"Manager",pay)

    def giveRaise(self, percent, bonus = 0.1):
        Person.giveRaise(self,percent + bonus)
    
class Department:
    def __init__(self,*args):
        self.members = list(args)

    def addMember(self,person):
        self.members.append(person)

    def giveRaises(self,percent):
        for person in self.members:
            person.giveRaise(percent)

    def showAll(self):
        for person in self.members:
            print(person)


if __name__=="__main__":
    vital = Person("Vital Muzalovs")
    marina = Person("Marina Jakovenko","Superviser",1000)

    print(vital.__dict__)
    print(marina.__dict__)

    print(marina.getSurname())
    print(vital.getSurname())
    
    marina.giveRaise(0.2)
    print(marina.getSurname(),'–>',marina.pay)

    print(marina)

    alex = Manager(name = "Alex Morozov",pay=2000)
    alex.giveRaise(0.2)
    print(alex)

    people = [vital,marina,alex]
    print("\n### All employees ###\n")
    for object in people:
        object.giveRaise(0.25)
        print(object)

    myDept = Department(marina,alex)
    print('\n### Department ###\n')
    myDept.giveRaises(0.2)
    myDept.showAll()
