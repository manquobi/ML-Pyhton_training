from ast import excepthandler
import os
from sqlite3 import SQLITE_DBCONFIG_LEGACY_FILE_FORMAT

os.system("cls" if os.name == "nt" else "clear")

num1 = float(input('enter first number: '))
operator = input('enter an operator (+ - * /): ')
num2 = float(input('enter second number: '))

user_input = num1, operator, num2
if user_input == 'quit':
    pass    

if operator == '+':
    result = num1 + num2
    print(f'{num1} + {num2} = ', result)

elif operator == '-':
    print(f'{num1} - {num2} = ', num1 - num2)
elif operator == '*':
    print(f'{num1} x {num2} = ', num1 * num2)
elif operator == '/':
    if num2 == 0:
        print('Error: cannot divide by zero')
    else:
        print(f'{num1} ÷ {num2} = ', num1 / num2)


else:
    print('Invalid input')
