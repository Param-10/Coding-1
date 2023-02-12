#Name: Paramveer Singh Bhele
#U-Number: U82076898
#Description: Factorial of a number - Assignment 3 - Take a nonnegative integer as an input and then check if it is positive or not. 
#If the input is 0 then the factorial is 1 and if the input is less than 0 then the program ends. 
#Factorial is calculated using while loop then factorial is found by multiplying it by factorial and i. i is then incremented 
#------------------------------------------------------------------
num = int(input('Enter a nonnegative integer: '))
i=1
fact=1
if num<0:
    print('Please enter a non-negative number')
    quit()
elif num==0:
    print('The factorial of 0 is 1')
    quit()
while(num>0):
        if(i<=num):
         fact=fact*i
         i=i+1
        else:
            break
print("The factorial of",num,"is",fact)
