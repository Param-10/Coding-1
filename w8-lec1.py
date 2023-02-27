#COP 2510 Week 8 Section 2 lecture 1

#function that returns a dictionary
def meaning():
    translate={'ngl':'not gonna lie','yeet':'throw'}
    return translate

#recursive function - function that calls itself
#design this carefully;avoid infinite recursion
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)


#lamda functions-small anonymous function
#can accept multiple parameters, but ONE expression
val=lambda x: x-5
#to call a function without a variable, you can copy the definition
#to your shell in (), then call using ()
#e.g. (lambda x:x-5)(10)




#----main function definition-----

def main():
    #call meaning function
    tr=dict()#creating empty dictionary
    tr=meaning()
    print(f'Here are some words and their meanings:\n{tr}')

    #test recursive function
    number=int(input('Enter a number>0:'))
    print(f'{number}!={factorial(number)}')

    #call lamba function using previous input
    print(f'{number}-5={val(number)}')
    print(val)

    #lambda functions can be combined with other convenient operations
    #e.g. lamba function with conditional form
    #note this is in main function definition
    maxval=lambda a,b:a if a>=b else b

    #test maxval
    n1,n2=input('enter two numbers(seperated by a space):').split()
    n1,n2=float(n1),float(n2)
    print(f'The larger of {n1} and {n2} is {maxval(n1,n2)}')


#----call to main-----
main()
