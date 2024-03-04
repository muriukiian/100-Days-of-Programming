#functions in python
#arbitrary arguments *args
def add_num(*nums):
  sum = 0
  for num in nums:
    sum += num
  return sum
print(add_num(3,4,5,6,4,6,6,3,7))

#Arbitrary keyword arguments **kwargs
def add_ages(**ages):
  sum = 0
  for l, j in ages.items():
    sum+= j
  return sum
print(add_ages(muchemi = 50, Kariuki = 35, Esther = 45))

def add_nums(a, b):
  answer = a + b;
  def double_it():
    double = answer * 2
    print(double)
  double_it()
  return answer

print(add_nums(2,13))

