#COP WEEK 9 LEC 2
#-----------dictionaries vs match cases--------
month=input('enter a month')
season={'january':'winter',
        'february':'fake spring',
        'March':'second winter'}

print(f'in {month} we experience {season.setdefault(month)} in florida')

#match case- python 3.10 or higher
seasons=''
match month:
    case 'January':
        seasons = 'winter'
    case 'February':
        seasons = 'fake spring'
    case 'March':
        seasons = 'second winter'

print(f'in {month} we experience {seasons} in florida')

n=int(input('enter the dictionary size:'))
d=dict()

for x in range(n):
    d[x]=x*3
print(d)

d[1]=x*3
print(d)

#for hardcoded duplicates, the most recent version can be used
d[1]=15
d.update({15:45})
d[70]=345
print(d)

#to remove values/pairs, use pop or popitem
d.pop(2)#passing key as arg
print(d)

d.popitem()#remove the most recent key value pair
print(d)
