#Name: Paramveer Singh Bhele
#U-Number: U82076898
#Description: Exponents using recursion - Assignment 4 - First, define 2 functions. One should be the main and the other should be the function which will calculate the power.
#In the Calculateower function, if the exponent is equal to 0 then the function will return 1 as the value. Even though the program will not accept 0 as the exponent, I have included this.
#In else, I have used recursion and called the same function again. I have multiplied the base by the result of the recursive call.
#The main function, takes a base and an exponent as input from the user. The while loop checks whether the exponent is less than 2 or greater than 50.
#If the while condition is true then the user will have to input another exponent. The value from the function is stored in a variable.
#The main function will print the output statement and then the main() is called. 
#-----------------------------------------------------------------------------------------------

def Calculatepower(base,exponent):
    if exponent == 0:
        return 1
    else:
          return base*Calculatepower(base,exponent-1)

def main():
    base = int(input("Enter the base: "))
    exponent = int(input("Enter a whole number between 2 and 50: "))
    while exponent < 2 or exponent > 50:
        exponent = int(input("Invalid. Please enter a whole number between 2 and 50: "))
    answer=Calculatepower(base,exponent)
    print(f"{base} raised to the power of {exponent} is {answer}")
    
if __name__ == "__main__":
    main()
