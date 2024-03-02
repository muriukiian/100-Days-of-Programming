#Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.
user_list = []
for i in range(5):
  user_number = int(input("Enter your unique number: "))
  user_list.append(user_number)
sum1 = 0
for user in user_list:
  sum1 += user
print(sum1)
#print(f'The list of integers is {user_list}.')

#Create a tuple containing the names of five of your favorite books. Then, use a for loop to print each book name on a separate line.
favBooks = ('Harry Potter','Hardy books','Scooby doo series','Rich dad poor dad','The art of war')
for book in favBooks:
  print(book)

#Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.
person = {}
name = str(input('Enter your name: '))
age = int(input('Enter your age: '))
favColour = str(input('Enter your favorite colour: '))
person['name'] = name
person['age'] = age
person['favorite colour'] = favColour
print(f'Person info is {person}')

#Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets.
set_a = set({})
set_b = set({})
set_c = set({})
for i in range(5):
  number_set_a = int(input('Enter set_a number: '))
  number_set_b = int(input('Enter set_b number: '))
  set_a.add(number_set_a)
  set_b.add(number_set_b)
print(set_a)
print(set_b)
for num in set_a:
  for num2 in set_b:
    if num == num2: set_c.add(num)
print(set_c)

#Create a program that stores a list of words. Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.
words=[]
for i in range(5):
  myWords = str(input("Type a word then hit enter: "))
  words.append(myWords)
newList = []
for word in words:
  if len(word) % 2 != 0: newList.append(word)
print(f'Words with odd number of characters are {newList}')