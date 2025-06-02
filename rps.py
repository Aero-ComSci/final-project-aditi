print ("Okay so I was working on code for hangman but it's currently 12:25 AM and the code isnt wokring :((( so Im switiching to rock papaer scisors vs computer")
print ("")
import random
import time
## I found stuff about import time online
RPS = ["rock", "paper", "scissors"]
playAgain = True
while playAgain:
    def compChoice():
        return random.choice(RPS)
    CC = compChoice()
    userInput=input("Pick rock, paper or scissors!")
    print (userInput, CC)
    while userInput.lower() not in RPS:
        userInput=input("I'm sorry but thats not a valid input! Pick rock, paper or scissors!")
        userInput = userInput.lower()
    else:
        print("The computer is now making its choice!!")
        for each in range (3,0,-1):
            time.sleep(.4)
            print (each, "...", end="")
        print("\n The computer picked", CC)
        if userInput == CC:
            print ("Its a draw!")
        elif userInput == "paper" and CC == "rock":
            print ("You win!!")
        elif userInput == "scissors" and CC == "paper":
            print ("You win!!")
        elif userInput == "rock" and CC == "scissors":
            print ("You win!!")
        else:
            print ("You lose")
        a = input ("Would you like to play again?")
        a = a.lower()
        if a == "yes":
           playAgain = True
        else:
            playAgain = False
            print ("Okay! thank you for playing")
        
        
        
