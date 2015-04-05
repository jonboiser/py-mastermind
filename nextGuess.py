# This method implements the Knuth Minimax strategy for choosing the next 
# guess. The implementation is based on the verbal description on the
# Wikipedia article for 'Mastermind': 
#     https://en.wikipedia.org/wiki/Mastermind_(board_game)#Five-guess_algorithm
from getGuessHint import *
from listCodes import *
from itertools import groupby, dropwhile
from random import choice

NUMSYMBOLS = 6
SECRETLENGTH = 4
ALLCODES = listCodes(range(NUMSYMBOLS), SECRETLENGTH)

def nextGuess(guess, hint):
	# 1. Narrow the search space to only those guesses that would yield the same
	# hint as the last guess, under the assumption that the last guess is the secret.
	sameHint = lambda g: getGuessHint(g, guess) == hint
	consistent_guesses = listCodes(range(NUMSYMBOLS), SECRETLENGTH, sameHint)

	# 2. For each consistent guess, compute the distribution of possible hints
	# that would be returned, for all possible secrets. Return the frequency
	# of the most common hint.
	hintDist = lambda g: groupby(sorted([getGuessHint(g, code, True) for code in ALLCODES]))
	hintMaxFreq = lambda g: max([len(list(b)) for a, b in hintDist(g)])

	max_hint_freqs = [(g, hintMaxFreq(g)) for g in guesses]

	# 3. Choose a guess whose maximum hint frequency is the lowest among
	# all other possibilities. Here, we randomly choose among those.
	min_of_max = min(max_hint_freqs)
	next_guesses = [g for g, freq in max_hint_freqs]
	
	return list(choice(next_guesses))


