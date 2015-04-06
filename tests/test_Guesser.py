# Tests all possible secrets. This test takes about 30 minutes.
# This test is not exhaustive, in it doesn't test all possible
# first guesses.
import unittest
import sys
sys.path.append('..')
from Guesser import *
from Hinter import *
from listCodes import listCodes

# Utility function for testing the AI guesser.
def guessTester(secret):
    allcodes = listCodes('roygbp', 4)
    guesser = KnuthGuesser(allcodes)
    hinter = Hinter(secret)
    done = False
    i = 0
    
    hint = None
    while not done and i < 10:
        guess = guesser.getGuess(hint)
        hint = hinter.getHint(guess)
        
        if hint['position'] == 4:
            # print("Guessed in {} tries.".format(i))
            return i
        
        else:
            i = i+1

    if i >= 10:
        print("Computer failed.")

    return i

class TestGuesser(unittest.TestCase):
    def testEverySecret(self):
        allcodes = listCodes('roygbp', 4)
        for secret in allcodes:
            numguesses = guessTester(secret)
            print("Secret: ", secret, ". Guesses: ", numguesses)
            self.assertTrue(numguesses < 10)

if __name__ == '__main__':
    unittest.main()
