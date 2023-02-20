year=int(input('enter the year'))
if year%4==0 and year%100!=0:
    print(f'{year} - leap year')
elif year%400==0:
    print(f'{year} -  leap year')
else:
    print(f'{year} - not a  leap year')