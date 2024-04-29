class Human:
    def setgender(self, g):
        self.gender = g
    def getgender(self):
        return self.gender
obj1=Human()
obj1.setgender("male")
print(obj1.getgender())
obj2=Human()
obj2.setgender("female")
print(obj2.getgender())
