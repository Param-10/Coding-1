#week6 lecture 2

#scope - visibility/accessibility of an identifier
#global scope - identifiers declared OUTSIDE of function or block
#local scope - identifiers declared INSIDE of function or block

x=15 #global variable (not a good idea): global constants are a great idea

#----function definitions------
def vofun1():
    print(f'In vofun1: the value of x is {x}')

def vofun2(x): #parameters are local to their functions
    x+=2
    print(f'In vofun2: the value of x is {x}')

def main():
    vofun1()
    x=5 #local variable
    print(f'In main: the value of x is{x}')



#---call to main----
main()



