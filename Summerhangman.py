import random

words = ["summer", "break", "freedom", "vacation", "tacos", "hot", "sun", "glasses", "beach", "travel", "swimming", "games", "home", "airplane"]
incorrectLet = []
game = True
GuessList = []
def wordGen():
    x = random.choice(words)
    under = (len(x))
    abe = 8
    game = True
    print (under, x)
    for each in range (under):
        print ("_", end=" ")
    def letterCheck():
        guess = input ("\nGuess a letter!\n")
        GuessList.append(guess)
        CorLetNum = 0
        while len(guess) > 1 or guess == " " or guess == "":
            print ("Thats not a valid input! Try again!")
            guess = input ("\nGuess a letter!\n")
            GuessList.append(guess)
        o=-1
        for y in GuessList:
            o = o+1
            for each in x:
                if GuessList[o] == each:
                    print (each, end=" ")
                    CorLetNum = CorLetNum +1  
                #else:
                 #   print ("_",end=" ")

        if CorLetNum==0:
            print ("Uh oh! thats not in the word!!!!")
            incorrectLet.append(guess)
        print("Trash:", incorrectLet)
    while game:            
        letterCheck()
        abe = abe - 1
        if abe < 1:
            game = False
        else:
            print ("you have", abe, "attempts left!")
    print (under)
    return under, x

print (wordGen())