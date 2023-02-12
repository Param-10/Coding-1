#Name: Paramveer Singh Bhele
#U-Number: U82076898
#Description: Good ol’ Guessing Game - Assignment 3 - I imported the random package to select a random integer from 1 to 100. Then I take the guess as an input.
#The while loop checks if the number of chances is less than 10 as the player has only 10 chances.
#The first if statement checks if the guess is not equal to the number and if the guess is higher than number but less than 100 then it shows a message 'too high'
#The elif statement checks if guess is not equal to the number and if the guess is less than the number but above 0 then it shows a message 'too low'
#2nd elif statement checks if the guess is equal to the random number and then displays the messages while also showing the number of chances taken by the player.
#3rd elif statement checks if the guess is less than or equal to 0 then it asks the player to enter the next guess.
#4th elif statement checks if the guess is above 100 then it asks the player to enter the next guess. 
#The else statement is executed once the player has extinguished all their 10 chances and it displays the correct number.
#-----------------------------------------------
import random
num=random.randint(1,100)
guess=int(input('Enter a number between 1 and 100 (inclusive): '))
chances=1
while(chances<10):

    if(guess!=num and guess>num and guess<=100):
        guess=int(input('Too high. Enter another guess: '))
        chances+=1
    elif(guess!=num and guess<num and guess>0):
        guess=int(input('Too low. Enter another guess: '))
        chances+=1
    elif(guess==num):
        print(f'You guessed it right!! You got it in {chances} guesses! ')
        quit()
    elif(guess<=0):
        guess=int(input('Really? Enter another guess between 1 to 100: '))
        chances+=1
    elif(guess>100):
        guess=int(input('Very funny. Enter a number between 1 and 100 (inclusive): '))
        chances+=1
else:
    print(f'Sorry, the number was {num}')
