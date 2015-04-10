class Hinter:
    """
    Creates a Hinter object, which is constructed with the secret.
    Receives guesses, and responds with a hint either as a dictionary
    or a tuple (in cases that the hint needs to be sortable).

    Examples:
    hinter = Hinter('prop')
    hinter.getHint('poor') #=> {'color': 1, 'position': 2}
    hinter.getHint('poor', True) #=> (1, 2)
    """
    def __init__(self, secret):
        self.secret = secret

    def getHint(self, guess, as_tuple = False):
        N = len(guess)
        assert N == len(self.secret), "Guess must be same length as the code."
        num_position = 0
        num_color = 0
    
        # Storage for guess/true code elements not matched exactly.
        guess_remainder = []
        secret_remainder = []
    
        # First pass to look for exact matches.
        for i in range(N):
            if guess[i] == self.secret[i]:
                num_position += 1
            else:
                guess_remainder.append(guess[i])
                secret_remainder.append(self.secret[i])
    
        # Second pass of remainders to see if guess has matched colors.
        for x in set(secret_remainder):
            if x in guess_remainder:
                num_color += 1
    
        # Option to return as tuple for cases when hints need to be sortable.
        if as_tuple:
            return (num_color, num_position)
        else:
            return {'color' : num_color, 'position': num_position }
 