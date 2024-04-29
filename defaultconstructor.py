class Employee:
    def __init__(self):
        self.name = 'Thinley'
        self.age = 20
    def displayEmployee(self):
        print(f'Name:{self.name} age:{self.age}')
e1 = Employee()
e1.displayEmployee()