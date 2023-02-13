arrowbaseheight = int(input())
arrowbasewidth = int(input())
arrowheadwidth = arrowbasewidth

while arrowheadwidth <= arrowbasewidth:
   arrowheadwidth = int(input())
for i in range(arrowbaseheight):
   for j in range(arrowbasewidth):
       print('*', end='')
   print()
for i in range(arrowheadwidth):
   for j in range(arrowheadwidth-i):
       print('*', end='')
   print()
