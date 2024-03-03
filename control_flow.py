#if, if...else, if elif else, and match case control flows
names=['John', 'Kate', 'Eric', 'Faith', 'Carol', 'Damaris', 'Hannah', 'Alice', 'Lucy', 'Irene', 'Natalia', 'Susan']
odd_names=[]
for name in names:
  if len(name) % 2 != 0: odd_names.append(name)
print(odd_names)

names=['John', 'Kate', 'Eric', 'Faith', 'Carol', 'Damaris', 'Hannah', 'Alice', 'Lucy', 'Irene', 'Natalia', 'Susan']
even_names=[]
odd_names2=[]
for name in names:
  if len(name) % 2 == 0 : even_names.append(name)
  else:odd_names2.append(name)
print(even_names)
print(odd_names2)

age = float(input("How old are you? "))
if age<18: print("Under age people cannot vote or drink alcohol in this country.")
elif 18<age<21: print("You can vote but no alcohol for you")
elif 21<age<=40: print("Vote first before going for a drink.")
elif 40<age<=80: print("Vote and go home. Alcohol does no good to your body.")
else: print("You can stay home if you wish. You have done our country proud!!")