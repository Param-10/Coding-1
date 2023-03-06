#Name: Paramveer Singh Bhele
#U-Number: U82076898
#Description: Basic operations using lambda functions - Assignment 4
#I have used the lambda functions for all of the operations(addition, subtraction, multiplication, floating point division, integer division, modulus and exponent).
#The compute function checks the parameters with the if conditions. It then computes the values and then returns the values obtained from the lambda functions.
#If an operator which is not present in the conditions is entered then the user will be prompted to enter the correct operators only. 
#In the main function, the value for the operator is taken as an input along with two numbers and the split function is used because it is specified in the question.
#The value returned from the compute function is then stored in the result variable.
#If the result value is not None then the expression is printed properly, otherwise if the operator was wrong then it just prints invalid operation.
#Lastly, the main() is called.
#-----------------------------------------------------------------------------------------------

add = lambda x, y: x + y
subtract = lambda x, y: x - y
multiply = lambda x, y: x * y
floating_point_division = lambda x, y: x / y
integer_division = lambda x, y: x // y
modulus = lambda x, y: x % y
exponent = lambda x, y: x ** y

def compute(operation, x, y):
    if operation in ['add', '+']:
        return add(x, y)
    elif operation in ['subtract', '-']:
        return subtract(x, y)
    elif operation in ['multiply', '*']:
        return multiply(x, y)
    elif operation in ['divide', '/']:
        return floating_point_division(x, y)
    elif operation in ['integer divide', '//']:
        return integer_division(x, y)
    elif operation in ['modulus', '%']:
        return modulus(x, y)
    elif operation in ['exponent', '**']:
        return exponent(x, y)
    else:
        return None

def main():
    operation = input("Enter the operation as a symbol (e.g. + for addition): ")
    x, y = input("Enter two values, separated by a space: ").split()
    x = float(x)
    y = float(y)
    result = compute(operation, x, y)
    if result is not None:
        print(f"{x} {operation} {y} = {result}")
    else:
        print(f"{x} {operation} {y} = Invalid operation")

if __name__ == "__main__":
    main()
