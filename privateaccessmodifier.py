class privateAM:
    __name = None
    def __init__(self, name):
        self.__name = name
    def __displaydetails(self):
        print("Name:",self.__name) #private Access Modifier

    def accessprivateFunction(self):
        self.__displayDetails()

obj = privateAM("hello")
obj.accessprivateFunction()