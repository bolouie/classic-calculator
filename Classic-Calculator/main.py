#Calculator Functions
from replit import clear
# HINT :You can call clear() to clear the output in the console.

from art import logo

def add(n1, n2):
	return n1 + n2


def subtract(n1, n2):
	return n1 - n2
	

def multiply(n1, n2):
	return n1 * n2
	

def divide(n1, n2):
	return n1 / n2

#Dictionary for calculator
#key: value pairs
operations = {
	"+": add,
	"-": subtract,
	"*": multiply,
	"/": divide,
}


def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
	#loop through the dictionary and print out the symbol (key)
  for symbol in operations:
    print(symbol)
	#flag variable
  should_continue = True
 
  while should_continue:
		#ask user to choose operation (saved to new variable)
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
		#purpose of outputs in form of return statements coded within operation functions as above
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()

calculator()
