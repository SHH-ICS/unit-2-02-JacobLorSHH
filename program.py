# My Python Program
# Task:  Use the function myFunction to output a simple "Hello World!" statement

def myFunction(name="", age=0, HadBirthday=None):
  if HadBirthday == True:
    age += 1  
  return str(name) + "was born in " + str(int(2023 - age))
#MyFunction

Username = input('What is your name?')
Age = int(input('How old are you?'))
Birth = input('Have you had your birthday this year?')
if Birth.lower == 'y':
  Birthday = True
print(myFunction(name=Username, age=Age, HadBirthday=Birth))
