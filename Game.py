from functools import reduce
from colorPrint import *
from Hinter import Hinter
from Guesser import KnuthGuesser
from listCodes import listCodes

class Game():
    """
    A Game object wraps the game logic and user interface.
    Currently, the number of symbols is hardcoded to 6 and the code length
    is hardcoded to 4. Also, the only game mode is with a human secret keeper
    and computer guesser.
    """
    symbols = 'roygbp'
    secretlength = 4

    def __init__(self):
        self.allcodes = listCodes(self.symbols, self.secretlength)
        self.guesser = KnuthGuesser(self.allcodes)
        print("Let's play Mastermind!")
        self.getSecret()
        self.guessSecret()

    def getSecret(self):
        print("Choose your secret, human. But don't show me!")
        print("\nWrite your code using these symbols:")
        print(colorPrint("'r' for 'red'", 'r'))
        print(colorPrint("'o' for 'orange'", 'o'))
        print(colorPrint("'y' for 'yellow'", 'y'))
        print(colorPrint("'g' for 'green'", 'g'))
        print(colorPrint("'b' for 'blue'", 'b'))
        print(colorPrint("'p' for 'purple'", 'p'))
        
        valid = False
        while not valid:
            secret = input("What is your secret? ")
            valid = self.__validateSecret(secret)

        self.hinter = Hinter(secret)

    def guessSecret(self):
        print("\nI will now guess your weak sauce code in less than 10 tries!")
        hint = None
        for i in range(10):
            guess = self.guesser.getGuess(hint)
            hint = self.hinter.getHint(guess)
            print("Guess #{}: {}".format(i, coloredCode(guess)))
            print("Hint: {} correct colors, ".format(hint['color']),
                "{} correct positions\n".format(hint['position']))
            if hint['position'] == self.secretlength:
                print("Ha! I got it!")
                return

    def __validateSecret(self, secret):
        valid = False
        right_length = len(secret) == self.secretlength
        right_symbols = reduce(lambda acc, sec: acc & (sec in self.symbols), secret, True)
        
        if not right_length:
            print("Your secret needs to be exactly " + 
                "{} characters.".format(self.secretlength))
            return False
        
        elif not right_symbols:
            print("Your secret can only contain the symbols r, o, y, g, b, p.")
            return False
        
        else:
            return True
   