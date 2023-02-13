#intro to functions

#void function
def fun1():
    print('this output statement is in a void function')

#value returning function
def trival(y):#y is a parameter-object referenced in function header
    print(f'the value obtained was {y}')
    y*=3
    return y

#main portion
fun1()#calling function

a=int(input('enter a number:'))
