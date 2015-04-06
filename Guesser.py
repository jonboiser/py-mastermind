from random import choice
from itertools import groupby
from Hinter import Hinter
from listCodes import listCodes

class KnuthGuesser:
    """
    The KnuthGuesser object implements a Minimax strategy for choosing the
    next guess.        
    """
    def __init__(self, allcodes):
        self.searchspace = allcodes[:]
        self.hinters = [Hinter(code) for code in allcodes]
        self.guesshistory = []
    
    def getGuess(self, hint = None):
        # If there is no hint, return a random code.
        if hint == None:
            self.guesshistory.append(choice(self.searchspace))
            return self.guesshistory[-1]
        
        # Update search space with hint.
        self.__updateSearchspace(hint)

        # Get the maximum hint frequency for each guess in the search space.
        max_hint_freqs = [(g, self.__hintMaxFrequency(g)) 
            for g in self.searchspace]
        
        # Get the mininum of those max frequencies (Minimax).
        min_of_maxes = min([freq for code, freq in max_hint_freqs])

        # Next guess is one of the codes with the minimal of the max hint
        # frequencies.
        next_guesses = [ code for code, freq in max_hint_freqs 
            if freq == min_of_maxes ]
        
        self.guesshistory.append(choice(next_guesses))
        return self.guesshistory[-1]

    def __updateSearchspace(self, hint):
        # Use the latest hint, and the last guess to filter the code
        # search space for only those codes that would return the
        # same hint, if the last guess were the secret.
        lastguess = self.guesshistory[-1]
        sameHint = lambda g: Hinter(lastguess).getHint(g) == hint
        self.searchspace = list(filter(sameHint, self.searchspace))

    def __hintMaxFrequency(self, guess):
        # Given a guess, for every possible secret, get the hint that would
        # be returned if the guess was submitted against the secret.
        all_hints = [hinter.getHint(guess, True) for hinter in self.hinters]
        hint_groups = groupby(sorted(all_hints))
        hint_dists = [len(list(freq)) for hint, freq in hint_groups]
        return max(hint_dists)
