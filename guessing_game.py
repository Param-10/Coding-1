import random
num=random.randint(1,100)
guess=int(input('Enter a number between 1 and 100 (inclusive): '))
chances=0
while(chances<10):
    if(guess!=num and guess>num):
        guess=int(input('Too high. Enter another guess: '))
        chances+=1
    elif(guess!=num and guess<num):
        guess=int(input('Too low. Enter another guess: '))
        chances+=1
    elif(guess==num):
        print(f'You guessed it right!! You got it in {chances} guesses! ')
        quit()
