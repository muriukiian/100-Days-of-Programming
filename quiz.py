def outer_fun(a, b):
    def inner_fun(c, d):
        return c + d
    return inner_fun(a, b)

res = outer_fun(5, 10)
print(res)
for num in range(1, 5):
    print(num)

for l in range(0,5,1):
  print(l)

list1 = [3 , 2 , 5 , 6 , 0 , 7, 9]
sum1 = 0
sum2 = 0
for elem in list1:
   if (elem % 2 == 0):
      sum1 = sum1 + elem
      continue
   if (elem % 3 == 0):
      sum2 = sum2 + elem
print(sum1 , end=" ")
