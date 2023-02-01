#Name: Paramveer Singh Bhele
#U-Number:  U82076898
#Description: First I checked whether the numerator and the denominator were negative or not
#Next I calculated the gcd and took another 2 variables to store the values in case the numerator and denominator are divisible by the gcd
#Next I used if else to check if numerator is less than denominator then it will be a proper fraction otherwise an improper fraction
#To convert it into a mixed fraction I found out the quotient and then the modulus operator to convert it into mixed fraction form.
#Next I checked if the remainder is 0 then it can be converted into a whole number.


import math

num=int(input('Enter a numerator:'))
if num<=0:
    num=int(input('Please Re-enter the numerator. Value must be greater than 0:'))

denom=int(input('Enter a denominator:'))
if denom<=0:
    denom=int(input('Please Re-enter a denominator. Value must be greater than 0:'))

gcd=math.gcd(num,denom)
num2=int(math.fabs(num/gcd))
denom2=int(math.fabs(denom/gcd))


if(num<denom):
    if num%gcd==0 and denom%gcd==0 and gcd!=1:
        print('{}/{} is a proper fraction \n'.format(num,denom))
        print('This proper fraction can be further reduced to {}/{}'.format(num2,denom2))

    else:
        print('{}/{} is a proper fraction \n'.format(num,denom))
        print('This proper fraction cannot be reduced any further.')

else:
    a=int(math.fabs(num//denom))
    b=int(math.fabs(num%denom))
    if num%gcd==0 and denom%gcd==0 and gcd!=1:
         a2=int(math.fabs(num2//denom2))
         b2=int(math.fabs(num2%denom2))
         print('{}/{} is an improper fraction \n'.format(num,denom))
         print('This improper fraction can be reduced to: {}/{}\n'.format(num2,denom2))
         if b2==0:
              print('The whole number is {}'.format(a2))
         else:
             print('The mixed number is {} and {}/{}'.format(a2,b2,denom2))
    else:
        print('{}/{} is a improper fraction \n'.format(num,denom))
        print('This improper fraction cannot be reduced any further.\n')
        if b==0:
              print('The whole number is {}'.format(a))
        else:
             print('The mixed number is {} and {}/{}'.format(a,b,denom))





