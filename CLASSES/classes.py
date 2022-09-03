from xml.sax import default_parser_list


class Shop:
    def __init__(self,name,size,address=None):
        self.name = name
        self.size = size
        self.address = address
        self.deptList = []
    
    def addDept(self,deptName):
        self.deptList.append(deptName)
    
    def showDepts(self,deptList):
        return print(k.name for k in self.deptList)

    def __str__(self):
        return f"""My shop name: {self.name}\tShop size: {self.size}\tAddress: {self.address}\nDepartments
---------------\n{self.showDepts}"""


class Department(Shop):
    def __init__(self,name):
        self.name = name


if __name__ == "__main__":
    rimi = Shop("Rimi","Hiper","K.Zales laukums")
    maxima = Shop("Maxima","XL")
    deptBread = Department("Bread")
    deptFish = Department("Fish")
    deptVegetables = Department("Vegetables")

    rimi.addDept(deptBread)
    rimi.addDept(deptFish)
    print(rimi)
    print(maxima)
