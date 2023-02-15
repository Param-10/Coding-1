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

def pythag(sidea,sideb):
    hyp=(sidea**2+sideb**2)**0.5
    return hyp

def main():
    vofun1()
    x=5 #local variable(great idea)
    print(f'In main: the value of x is{x}')
    vofun2(x)

    sidea, sideb=input('enter sides a and b for a right triangle:(seperated by a space):').split()
    sidea=float(sidea)
    sideb=float(sideb)

    print(f'the hypotenuse is {pythag(sidea,sideb)}')

    #test default paramters
    printdate(2,15)
    printdate(2,15,2027)
    printdate(2,15,2027,3)
    #printdate(2)#does not work

    #use lol stats(w/o keyboard arguements)
    lolstats('female',178,'Vi',24)#values are in wrong order
    #use lol stats(w/ keyword arguements)
    lolstats(gender='female', height=178, name='Vi', age=24)#values are still in wrong order



#this function uses default parameters-parameters with built in values
#default parameters must appear after positional parameters

def printdate(month,day,year=2023, style=1):
    if style==1:
        print(f'{month}/{day}/{year}')
    elif style==2:
        print(f'{day}/{month}/{year}')
    elif style==3:
        print(f'{year}/{month}/{day}')
    else:
        print('invalid')

def lolstats(name,age,gender,height):
    print(f'\nName:{name}\nAge: {age}\nGender: {gender}\nHeight: {height}')
    



#---call to main----
main()



