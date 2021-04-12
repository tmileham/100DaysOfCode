#Calculator
def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

app_running = True

num1 = float(input("What's the first number?: "))
for symbol in operations:
  print(symbol)

while app_running:
  operation_symbol = input("Pick an operation: ") 
  num2 = float(input("What's the next number?: "))
  calculation_function = operations[operation_symbol]
  answer = calculation_function(num1, num2)

  print(f"{num1} {operation_symbol} {num2} = {answer}")

 
  if input("Type 'y' to continue calculating with {answer}, or type'n' to exit. :") == "y":
    num1 = answer
  else:
    app_running = False # could also have used break


  # operation_symbol = input("Pick an operation: ") 
  # num3 = int(input("What's the next number?: "))

  # calculation_function = operations[operation_symbol] 

  # second_answer = calculation_function(answer, num3)

  # print(f"{answer} {operation_symbol} {num3} = {second_answer}")

