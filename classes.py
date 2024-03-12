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

#INHERITANCE
#1. single inheritance
#Base/parent class
class Vehicle:
  def vehicleInfo(self):
    print("Inside parent(Vehicle) class")

#Child class
class Car(Vehicle):
  def carInfo(self):
    print("Inside child(car) class")

#Create an object car
car = Car()
#Access vehicle info using car class
car.vehicleInfo()
car.carInfo()

#2. Multiple inheritance
class Person:
  def personInfo(self,name,age):
    print("Inside Person class")
    print('Name: ',name,'Age: ',age)

class Company:
  def companyInfo(self,companyName,location):
    print('Inside companyInfo class')
    print('companyName: ',companyName,'Location: ',location)

class employee(Person, Company):
  def employeeInfo(self,salary,skill):
    print("Inside employee class")
    print('Salary: ',salary,'Skill: ',skill)

#create an object of employee
emp = employee()
#fetch data
emp.personInfo('Ian',27)
emp.companyInfo('Tesla', "Texas")
emp.employeeInfo(12000,'Software engineer')

#3. Multi-level inheritance
class  Vehicle:
  def vehicle_info(self):
    print("inside vehicle class")

class Car(Vehicle):
  def car_info(self):
    print("inside the car class")

class super_car(Car):
  def super_car_info(self):
    print("inside super_car class")

#create an object of super_car
s_car1 = super_car()
#access data from vehicle and car class using super_car object
s_car1.vehicle_info()
s_car1.car_info()

#4. Heirarchial inheritance.
class Vehicle:
  def vehicleinfo(self):
    print('This is a vehicle.')
class Car(Vehicle):
  def carinfo(self, name):
    print('Name of the car is ', name)
class Truck(Vehicle):
  def truckInfo(self,name):
    print('Name of truck is ',name)

obj1 = Car()
obj1.vehicleinfo()
obj1.carinfo('BWM')

obj2 = Truck()
obj2.vehicleinfo()
obj2.truckInfo("Mercedes Actros")

#5. Hybrid inheritance
class Vehicle:
  def vehicleInfo(self):
    print("Inside vehicle class")

class Truck(Vehicle):
  def truckInfo(self):
    print("Inside truck class")

class Car(Vehicle):
  def carInfo(self):
    print("inside car class")

class SportCar(Car, Vehicle):
  def sportsCarInfo(self):
    print("Inside SportsCar class")

s_car3=SportCar()
s_car3.vehicleInfo()
s_car3.carInfo()
s_car3.sportsCarInfo()

#super() method ==> Makes the child class inherit all properties and methods from the parent class.
class Company:
  def companyName(self):
    return "Google"
class Employee(Company):
  def info(self):
    c_name=super().companyName()
    print("Jessa works at ",c_name)

emp=Employee()
emp.info()

#issubclass() ==> used to check whether a class is a subclass of another class.
class Company:
  def companyInfo(self):
    print('All company info')

class Employee(Company):
  def employeeInfo(self):
    print('All employee info')

class Player:
  def playerInfo(self):
    print('All player info.')

print(issubclass(Employee, Company)) #true
print(issubclass(Player,Company)) #false