#COP 2510 WEEK 5 LECTURE 1

#loop else
for i in range(1,5):
    print(i)
else:
    print('Loop ran successfully.')

#loop else with break
for i in range(1,5):
    print(i)
    break
else: #skipped because loop didn't complete its iterations
    print('Loop ran successfully')

#loop else with continue
for i in range(1,11):
    if i==4:
        continue
    print(i)
else: #skipped because loop didn't complete its iterations
    print('Loop ran successfully')

#nested looops
#for every 1 iteration of the outerloop, the inner loop completes all iterations
digit1=0
while digit1<=9:
    digit2=0
    while digit2<=9:
        print(f'{digit1}...{digit2}')
        digit2+=1
    digit1+=1
    break

#nested for loop
for m in range(1,6):
    print()
    for n in range (1,11):
        print(f'{m}*{n}={m*n}')

#for loop with enumerate
for m,n in enumerate(range(1,11)):
    print(f'{m}*{n}={m*n}')

