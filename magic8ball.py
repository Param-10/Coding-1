#Name: Paramveer Singh Bhele
#U-Number: U82076898
#Description: Magic 8 Ball - Assignment 4
#First, I have imported random as it will be required to create a random resposnse from the magic 8 ball.
#Next I have defined the void function. I have crated a list called as response and then put all the responses in the list. The responses will be printed in the function itself.
#I have used x-1 as a list starts from 0.
#In the main function, the user inputs their question and then a random integer is created between 1 and 20. Then, the void function is called and rand is used as a parameter. 
#The random integer is used to select a response from the list. The user is then asked to ask another question.
#In the while loop, if the user says yes or not no then the loop is broken and the main function is called again. Else, if no is the input then the program ends.
#Lastly, the main() is called.
#-----------------------------------------------------------------------------------------------

import random

def void(x):
        response= ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]
        print(response[x-1])

def main():
    ques=input('What is your question? ')
    rand=random.randint(1,20)
    void(rand)
    nextq=input('Would you like to ask another question? ')
    nextq=nextq.lower()
    while nextq!='no':
          break
    else:
          quit()
    main()

if __name__ == "__main__":
    main()

