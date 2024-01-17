#a simple calculator
def calculate(op, a, b):
  if (op == '+'):
    return a + b
  elif (op == '-'):
    return a - b
  elif (op == '*'):
    return a * b
  elif (op == '/'):
    return a / b
  elif (op == '^'):
    return a**b
  else:
    return "Invalid operator"


history = []
while True:
  print("welome to the calculator\n")
  a = int(input("enter the first number\n"))
  b = int(input("enter the second number\n"))
  op = input("enter the operator\nif u want to exit enter 'e'\n")
  if op == 'e':
    break
  print(calculate(op, a, b))
