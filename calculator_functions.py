#calculator_functions.py  
#This file is a trimmed down functions file from a different calculator project

def add(n1, n2):
    return n1 + n2 

def subtract(n1, n2): 
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

#checks to see if divisor is zero
def divide(n1, n2):
    if n2 == 0:
        return "Error: Cannot divide by zero!"
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

#checks to see if operator is in Dictionary
def check_operator_input(operator_input): 
    if operator_input in operations: 
        return True 
    else: 
        return False

def calculate_number(num1,num2,operator):  
    #This function calculates the input that was given through the user data
    calculation_function = operations[operator]  #This line assigns the user operator to it's function in the Dictionary
    return calculation_function(num1, num2) 
   
