import os

os.system("cls" if os.name == "nt" else "clear")

i = 1
while i < 6:
    print(i)
    i += 1

i = 1
while i < 6:
    print(i)
    if i == 3:  # break Statement
        break
    i += 1

i = 0
while i < 6:
    i += 1
    if i == 3:  # continue Statement
        continue
    print(i)

i = 1
while i < 6:
    print(i)
    i += 1
else:  # else statement
    print("i is no longer less than 6")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

for x in "banana":
    print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":  # break statement
        break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":  # continue statement
        continue
    print(x)

for x in range(6):  # range function
    print(x)

for x in range(2, 6):
    print(x)

for x in range(2, 30, 3):
    print(x)

for x in range(6):
    print(x)
else:
    print("Finally finished!")

for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finally finished!")

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:       # NESTED LOOP
  for y in fruits:
    print(x, y) 

for x in [0, 1, 2]: # PASS statement
  pass