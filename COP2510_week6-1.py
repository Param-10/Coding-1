#intro to functions
#main function

def main():
    fun1()
    a=int(input('enter a number:'))
    b=tripval(a)#a is an arguement -  value or object referenced in a function call
    print(f'the value tripled is {a}')
    print(f'the value tripled is {b}')

#void function
def fun1():
    print('this output statement is in a void function')

#value returning function
def tripval(y):#y is a parameter-object referenced in function header
    print(f'the value obtained was {y}')
    y*=3
    return y

#effect of duplicate functions in python
#def main():
# print('This is a second main function.')

#def tripval(x,y,z):
  #  triple=x+y+z
  #  return triple
#------no function definitions below this line-------

main()#call to main
