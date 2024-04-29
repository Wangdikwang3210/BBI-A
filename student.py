class students:
    def setmodules(self, g):
        self.gender = g
    def getmodules(self):
        return self.gender
obj1=students()
obj1.setmodules("BIA")
print(obj1.getmodules())
obj2=students()
obj2.setmodules("BIA")
print(obj2.getmodules())