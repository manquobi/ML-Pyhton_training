import os

os.system("cls" if os.name == "nt" else "clear")

x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6)) 

x = lambda a, b, c : a + b + c
print(x(5, 6, 2)) 

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))


def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))


class MyClass:        #CLASSES/OBJECTS
  x = 5
print(MyClass)
p1 = MyClass()
print(p1.x) 

class Person:
    def __init__(self, name, age):
        self.name = name  # Assigning name to the instance
        self.age = age    # Assigning age to the instance

p1 = Person("John", 36)  # Creating an instance of Person with name "John" and age 36

print(p1.name)  # Output: John


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} is {self.age} years old"

p1 = Person("John", 36)

print(p1)  # Output: John is 36 years old