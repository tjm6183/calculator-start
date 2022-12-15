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
  "/": divide,
}

def calculator():
  num1 = int(input("What's the first number?: "))
  num2 = int(input("What is the second number?: "))
  
  for symbol in operations:
    print(symbol)
  
  operation_symbol = input("Pick an operation from the line above: ")
  
  if operation_symbol == "+":
    answer = add(num1, num2)
  elif operation_symbol == "-":
    answer = subtract(num1, num2)
  elif operation_symbol == "*":
    answer = multiply(num1, num2)
  elif operation_symbol == "/":
    answer = divide(num1, num2)
  
  print(f"{num1} {operation_symbol} {num2} = {answer}")
  
  continue_question = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")

  while continue_question == "y":
    operation_symbol = input("Pick an operation: ")
    next_number = int(input("What is the next number?: "))
    old_answer = answer
    
    if operation_symbol == "+":
      answer = add(answer, next_number)
    elif operation_symbol == "-":
      answer = subtract(answer, next_number)
    elif operation_symbol == "*":
      answer = multiply(answer, next_number)
    elif operation_symbol == "/":
      answer = divide(answer, next_number)

    print(f"{old_answer} {operation_symbol} {next_number} = {answer}")

    continue_question = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ")
  else:
    return
  
calculator()
