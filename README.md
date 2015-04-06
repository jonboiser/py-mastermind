# Mastermind

Screenshot:

![](http://g.recordit.co/JNspkCAMnu.gif)

## Installation

This program was written in Python 3, and relies on the `colorama` module for the colored terminal output, which can be installed via `pip`:

```
pip3 install colorama
```

The game can be played by invoking `letsPlay.py` script with the Python 3 interpreter.

## Contents

These are the current files in the repo:

* `Game.py`: Contains the definition for the `Game` class, which wraps the game logic and user interface (may later decouple the game and AI hinter logic, and add different game modes/classes).
* `Hinter.py`: Containe the definition for the `Hinter` class, which is initialized with the secret, and provides hints in response to guesses via its `Hinter.getHint(guess)` method.
* `Guesser.py`: Contains the definition for the `KnuthGuesser` class, which implements the Minimax strategy described in this [Wikipedia article](https://en.wikipedia.org/wiki/Mastermind_(board_game)).
* `listCodes.py`, `colorCode.py`: Utility functions for enumerating all the possible codes, and printing text and codes in color, respectively.
* `tests/`: The test suite for the different classes and methods.
