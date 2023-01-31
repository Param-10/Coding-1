#Name: Paramveer Singh Bhele
#U-Number: U82076898
#Description: The Price is Right! (One Bid) - Assignment 2: I have imported the random and math modules
#The first if statement checks if everyone has overbid
#The second if statement checks if any of the players have netered the correct answer
#Then I have compared the differences between each bid and original price
#The if and elif statements are used to compare all the differences and find out the lowest one which would make the player the winner. 
import random
import math

price=random.randint(1000,5000)

print('Please enter your bids in dollars(no cents)')
p1=int(input('Player 1, what is your bid?'))
p2=int(input('Player 2, what is your bid?'))
p3=int(input('Player 3, what is your bid?'))
p4=int(input('Player 4, what is your bid?'))
if p1>price and p2>price and p3>price and p4>price:
    print('Buzz! Aww... everyone has overbid! ')
    exit()

if p1==price or p2==price or p3==price or p4==price:
    print('Ding Ding Ding! One player got it exactly right and gets $500!')

closest1=math.fabs(price-p1)
closest2=math.fabs(price-p2)
closest3=math.fabs(price-p3)
closest4=math.fabs(price-p4)

if closest1<closest2 and closest1<closest3 and closest1<closest4:
    print(f'Actual price is {price}! Player 1, come on up! ')
elif closest2<closest1 and closest2<closest3 and closest2<closest4:
    print(f'Actual price is {price}! Player 2, come on up! ')
elif closest3<closest1 and closest3<closest2 and closest3<closest4:
    print(f'Actual price is {price}! Player 3, come on up! ')
elif closest4<closest1 and closest4<closest2 and closest4<closest3:
    print(f'Actual price is {price}! Player 4, come on up! ')

