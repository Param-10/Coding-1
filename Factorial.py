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