# Compare two codes, the "guess" and the "secret", and get the Mastermind
# hint of the number of correct positions, and the number of correct colors.
# The output is a dictionary object with keys "color" and "position".
#
# There is an `as_tuple` option for cases when the output needs to be sortable.
#
# Examples:
# getGuessHint([1,2,3], [3,1,2]) #=> {'color': 3, 'position': 0}
# getGuessHint([1,2,3], [3,1,2], True) #=> (3, 0)
def getGuessHint(guess, secret, as_tuple = False):
    N = len(guess)
    assert N == len(secret), "Guess must be same length as the code."
    num_position = 0
    num_color = 0

    # Storage for guess/true code elements not matched exactly.
    guess_remainder = []
    secret_remainder = []

    # First pass to look for exact matches.
    for i in range(N):
        if guess[i] == secret[i]:
            num_position += 1
        else:
            guess_remainder.append(guess[i])
            secret_remainder.append(secret[i])

    # Second pass of remainders to see if guess has matched colors.
    for x in set(secret_remainder):
        if x in guess_remainder:
            num_color += 1

    # Option to return as tuple for cases when hints need to be sortable.
    if as_tuple:
        return (num_color, num_position)
    else:
        return {'color' : num_color, 'position': num_position }
