#COP 2510 Section 2 Week 3 Lecture 1
#-----compound assignment statements-----
number=18
print(f'original number is {number}')
 #number = number + 2
number+=2
print(f'new number is {number}')

x=5
y=6
number *= x + y #20*(5+6)=20*11=220
#number = number * x + y = 20*5+6=100+6
print(f'new number is {number}')
number -=10
print(f'new number is {number}')
number /=7
print(f'new number is {number}')
number //=4
print(f'new number is {number}')
number%=10
print(f'new number is {number}')
number**=3
print(f'new number is {number}')

#-----random module (and aliasing)-----
import random as rn #rn - alias
r=rn.random()
print(f"Here's a random number between 0 and 1 (excel):{r:.7F}")
r=rn.uniform(1,45)
print(f"Here's a random number between 1 and 45:{r:.5f}")
r=rn.randint(1,6)
print(f"Here's a random number between 0 and 9:{r}")
r=rn.randrange(10)
print(f"Here's a random number between 0 and 9:{r}")
r=rn.randrange(2,17)
print(f"Here's a random number between 2 and 16:{r}")
r=rn.randrange(10,51,5)
print(f"Here's a random number between 10 and 50:{r}")

#------selection--------
#relational operators - <,>,<=,>=,==, !=
#logical operators - not, and , or

score = float(input('Enter a score:'))

#one way selection
if score>=80:
    print('Yay! You advance, congrats')
    print('Good job')

#walrus operator version
#two way selection
if score:=float(input('Enter a score:'))>80:
     print('Yay! You advance, congrats')
     print('Good job')
else:
     print('oh no, try again')