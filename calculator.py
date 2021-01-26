def add(x, y):
  return x + y
 
def subtract(x, y):
  return x - y

def mul(x, y):
  return x * y

def div(x, y):
  return x / y

operation = int(input("Enter your operation:\n\n1) Addition\n2) Subtraction\n3) Multiplication\n4) Division"))
if operation == 1:
  num1 = int(input("Enter a number: "))
  num2 = int(input("Enter another number: "))
  print(add(x, y))
 elif operation == 2:
  num1 = int(input("Enter a number: "))
  num2 = int(input("Enter another number: "))
  print(subtract(x, y))
 elif operation == 3:
  num1 = int(input("Enter a number: "))
  num2 = int(input("Enter another number: "))
  print(mul(x, y))
 elif operation == 4:
  num1 = int(input("Enter a number: "))
  num2 = int(input("Enter another number: "))
  print(div(x, y))
