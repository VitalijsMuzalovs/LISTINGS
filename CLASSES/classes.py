from xml.sax import default_parser_list


class Shop:
    def __init__(self,name,size,address=None):
        self.name = name
        self.size = size
        self.address = address
        self.deptList = []
    
    def addDept(self,deptName):
        self.deptList.append(deptName)
        
    def showDepts(self):
        print('\"',self.name,'\"'," departments:")
        if len(self.deptList)>0:
            for el in self.deptList:
                print(el )
        else:
            print("No departments")
            
    def __str__(self):
        return f"""My shop name: {self.name}\tShop size: {self.size}\tAddress: {self.address}\nDepartments"""
# ---------------\n{self.showDepts}"""


class Department():
    def __init__(self,depName):
        self.name = depName


if __name__ == "__main__":
    rimi = Shop("Rimi","Hiper","K.Zales laukums")
    maxima = Shop("Maxima","XL")
    deptBread = Department("Bread")
    deptFish = Department("Fish")
    deptVegetables = Department("Vegetables")

    rimi.addDept(deptBread.name)
    rimi.addDept(deptFish.name)
    rimi.showDepts()

    print(maxima)
    maxima.showDepts()

