#---multiple input---
#option 1 multiple input functions and one prompt
print('Enter 3 values(press"enter" after each)')
a=int(input())
b=float(input())
c=int(input())
print(f'The values entered were {a},{b} and {c}.')

#option 2- use input funtion and split the results
d,e,f=input('Enter 3 values(seperated by spaces):').split()

d=int(d)
e=float(e)
f=int(f)
print(f'The values entered were {d},{e} and {f}.')

