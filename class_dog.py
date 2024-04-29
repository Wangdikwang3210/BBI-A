class Dog:
     def __init__(self, breed, age, color):
          self.breed=breed
          self.age=age
          self.color=color
     def bark(self):
          print('moof! moof!')
     def sleep(self):
          print('Zzzzz....')

     def eat(self):
          print('Nom nom nom')
          

     
my_dog =Dog(breed="labrador retriever", age=3, color="golden")
print(f"my dog is a {my_dog.breed} {my_dog.color} and is{my_dog.age} years old")
my_dog.bark()
my_dog.sleep()
my_dog.eat()