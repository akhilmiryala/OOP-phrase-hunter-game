# Import your Game class

# Create your Dunder Main statement.

# Inside Dunder Main:
## Create an instance of your Game class
## Start your game by calling the instance method that starts the game loop
from game import Game

if __name__ == "__main__":
    # def print_phrase(phrase_object):
    #     print("The phrase is: {}".format(phrase_object.phrase))
    # game = Game()
    # print_phrase(game.get_random_phrase())
    # print_phrase(game.get_random_phrase())
    # print_phrase(game.get_random_phrase())
    # print_phrase(game.get_random_phrase())
    # print_phrase(game.get_random_phrase())
    
    # game = Game()
    # print(game.active_phrase)
    # print(game.active_phrase.phrase)

    game = Game()
    print(game.active_phrase.phrase)
    game.active_phrase.display(game.guesses)