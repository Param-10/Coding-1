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