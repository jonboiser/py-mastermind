import Game
import importlib
def main():
    g = Game.Game()
    playagain = input("Play again? (y/n): ")
    if playagain == "y":
        main()

if __name__ == "__main__":
    main()
