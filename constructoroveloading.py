
class ConstructorOverloading:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("age:", self.age)

obj1 = ConstructorOverloading()
obj2 = ConstructorOverloading("Alice")
obj3 = ConstructorOverloading("Bob", 30)

obj1.display()
obj2.display()
obj3.display()
