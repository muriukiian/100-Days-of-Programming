#Class attributes
class Cat:
  def _init_(self):
    self.name=""
    self.color=""

nora = Cat()
nora.name="Nora"
nora.color="White"
print(f'{nora.name} is a {nora.color} cat.')

#defining a constructor
class Person:
  def _init_(self): #constructor method
    print("Constructor invoked.")

person1 = Person()
print(person1)

#instance attributes
class Car:
  origin = "Germany" #class attribute
  def _init_(self): #Always specify values of instance attributes through the constructor.
    self.name = ""
    self.age = ""

volkswagen = Car()
volkswagen.name = "Volkswagen Passat"
volkswagen.age = "made in 2024"
print(f'The car is a {volkswagen.name} and was {volkswagen.age}')

#setting attribute values
class Person:
  def _init_(self,name,age):
    self.name=name
    self.age=age

#person3 = Person("Mutemi",65)
#person3.name
#person3.age

#class methods
class Person:
  def displayInfo(self):
    print("Print all my personal information.")

person4 = Person()
person4.displayInfo()

#PUTTING IT ALL TOGETHER
class Person:
  def _init_(self, name, age):
    self.name = name
    self.age = age
  def displayInfo(self):
    print(f'Name: {self.name}, Age: {self.age}')

person34 = Person()
person34.name = input("enter your name: ")
person34.age = input("enter your age: ")
person34.displayInfo()