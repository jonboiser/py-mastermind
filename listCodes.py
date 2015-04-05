# When given a set of symbols (usually a range of numbers), and a length,
# return a list of all possible combinations of those symbols (as tuples).
# This uses Python's itertools.product method, for convenience, but 
# coerces the output to a list, rather than keeping it as a generator.

# An optional predicate can be passed into the function to filter it.

# Example:
# listCodes(range(3), 4) #=> [(0,0,0,0), (0,0,0,1), (0,0,0,2), ..., (2,2,2,2)]
# listCodes(range(3), 4, lambda x: x[0] == 1) #=> [(1,0,0,0), ..., (1,2,2,2)]
from itertools import product

def listCodes(symbols, length, pred = lambda x: True):
	return list(filter(pred, product(symbols, repeat = length)))