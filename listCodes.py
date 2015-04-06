from itertools import product
from functools import reduce

def listCodes(symbols, length):
    if length == 0:
        return [] # consistent behavior when symbol or length = 0
    else:
        return [reduce(lambda a, b: a + b, x) 
            for x in product(symbols, repeat = length)]
