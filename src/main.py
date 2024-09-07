


import os
os.system('cls' if os.name == 'nt' else 'clear')


a = 33                            # IF, ELIF, ELSE
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

  a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

if a > b: print("a is greater than b") 

print("A") if a > b else print("B") 

print("A") if a > b else print("=") if a == b else print("B") 

a = 200
b = 33
c = 500
if a > b and c > a:                  #  AND
  print("Both conditions are True")

a = 200
b = 33
c = 500
if a > b or a > c:                                # OR
  print("At least one of the conditions is True")

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")              # NOT

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:                    # NESTED IF
    print("and also above 20!")
  else:
    print("but not above 20.") 

a = 33
b = 200

if b > a: # PASS STATEMENT
  pass