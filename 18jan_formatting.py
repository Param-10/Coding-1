from math import sqrt, ceil, fabs
import math


num=float(input('Enter a positive number:'))
print(f'The square root of {num} is {sqrt(num)}.')
print(f'The absolute value of {num} is {fabs(num)}.')
print(f'{num}rounded up is {ceil(num)}.')

#formatting options
#option1: use comma and the format function
print('The square root of',num,'is',format(sqrt(num),'.5f'))

#option 2: string formatting with %
age=8
print('My dog will be %d years in March.'%age)

#option 3: string formatting with format method
amount =12
price=8.3499
print('{}eggs now cost ${:.2f}'.format(amount,price))
print('You can save{:.1%} when you switch to GEICO.'.format(savings:=0.1499))

#option 4: formatting within the f-string
print(f'{amount}eggs now cost ${price:.2f}')
winnings=750000000
print(f'Alucky winner in Maine will receive ${winnings:,.2f}(before taxes).')