

# My first project in python.
# A simple calculator with 4 basics operations.

info_01 = print('Comands for operations! \n'
        '[+] ->  addition \n'
        '[-] -> Subtraction \n'
        '[*] -> Multiplication \n'
        '[/] -> division \n')

choise = input('Choise the operations: ')

def sum(x,y):
    soma = (x + y)

def sub(x,y):
    sub = (x - y)

def mult (x,y):
     mult = (x * y)

def div(x,y):
      div = (x - y)
      if div == 0:
           return 'Error! It is impossible to divison by 0'
      else:
           return (x/y)

if choise == '+':
     value1 = (float(input('Type it the first number: ')))
     value2 = (float(input('Type it the second number: ')))
     
     result = (value1 + value2)

     print(f'the result of sum is: {result}')

elif choise == '-':
     value1 = (float(input('Type it the first number: ')))
     value2 = (float(input('Type it the second number: ')))
     
     result = (value1 - value2)

     print(f'the result of sub is: {result}')

elif choise == '*':
     value1 = (float(input('Type it the first number: ')))
     value2 = (float(input('Type it the second number: ')))
     
     result = (value1 * value2)

     print(f'the result of mult is: {result}')

elif choise == '/':
     value1 = (float(input('Type it the first number: ')))
     value2 = (float(input('Type it the second number: ')))
     
     result = (value1 / value2)

     print(f'the result of div is: {result}')


else:
     print('Maybe you didn`t obey the rules')
