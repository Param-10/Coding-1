#Name: Paramveer Singh Bhele
#U-Number: U82076898
#Description: The Price is Right! (One Bid) - Assignment 2:  
import random
price=random.randint(1000,5000)
print('Please enter your bids in dollars(no cents)')
p=1
while(p<5):
    bid= int(input("Player "+str(p)+", what is your bid? "))
    if bid<=price:
        closest= price -bid
        

    
        

