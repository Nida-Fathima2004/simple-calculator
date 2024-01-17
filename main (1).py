#a simple calculator with memory 
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
  history.append(str(a)+op+str(b)+ "=" +str(calculate(op,a,b)))
  if op == 'e':
    break
  print(calculate(op, a, b))
  print("history=",history)
