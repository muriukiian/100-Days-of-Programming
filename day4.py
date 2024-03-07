#lambda functions.
isString = lambda input1 : 'Even length' if len(input1) % 2 == 0 else 'Odd length'
input1 = input('Enter a value: ')
print(isString(input1))

names=[]
for i in range(5):
  name=input('Enter name: ')
  names.append(name)
print(names)

#Create a method that tests whether the result of taking the power of one number to another number provides an answer which is greater than 5000
def largePower(base, exponent):
  result = base**exponent
  if result > 5000:
    return True
  else:
    return False
  
#Create a function that determines whether a number is divisible by 10
def divisible_by_ten(num):
  if num % 10 == 0:
    print(True)
  else:
    print(False)

divisible_by_ten(45)