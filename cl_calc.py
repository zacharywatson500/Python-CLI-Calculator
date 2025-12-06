#cl_calc.py

import argparse 
import calculator_functions

#Creates and argunent parser object
parser = argparse.ArgumentParser(description="A simple command-line calculator.") 

# This recieves the arguments in order of num1, operator, num2
parser.add_argument("num1", type=float, help="The first number in the calculation.")
parser.add_argument("operator", type=str, choices=['+', '-', '*', '/'], help="The math operator (+, -, *, /).") 
parser.add_argument("num2", type=float, help="The second number in the calculation.")

#Adding a verbose flag. Right now it only tells you if you divided a number by zero
parser.add_argument("-v", "--verbose", action="store_true", help="Print detailed calculation steps.")  

#Reads the parsed input and creates the args object
args = parser.parse_args()  

#Throws an error if the operator argument is incorrect
#if calculator_functions.check_operator_input(args.operator) == False: 
#    raise ValueError('The operator (second argument) must be "+", "-", "*" or "/"')

 # This bolck runs when -v or --verbose is typed
if args.verbose:
    print("--- DEBUG INFORMATION ---")
    print(f"Operation performed: {args.num1} {args.operator} {args.num2}")
    if args.num2 == 0 and args.operator == '/':
        print("Warning: Division by zero attempted. Returning error message.")
    else:
        print("Calculation complete. No errors detected.")
    print("-------------------------") 

#Calculates incoming arguments
solution = calculator_functions.calculate_number(args.num1,args.num2,args.operator)

# Printing user imputed values and solution
print(f"First Number: {args.num1}")
print(f"Operator: {args.operator}")
print(f"Second Number: {args.num2}")
print(f"Solution: " + str(solution))