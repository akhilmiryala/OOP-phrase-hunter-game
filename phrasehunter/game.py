from phrase import Phrase
import random

class Game:

    def __init__(self):
        setattr(self,'missed',0)
        setattr(self,'phrases',self.create_phrases())
        setattr(self,'active_phrase',self.get_random_phrase())
        setattr(self,'guesses',[" "])

    def create_phrases(self):
        phrase_list = []

        phrase1 = Phrase("Lebron James is the GOAT")
        phrase2 = Phrase("I am twenty one years old")
        phrase3 = Phrase("I love playing sports")
        phrase4 = Phrase("I love to read")
        phrase5 = Phrase("I love programming")

        phrase_list.append(phrase1)
        phrase_list.append(phrase2)
        phrase_list.append(phrase3)
        phrase_list.append(phrase4)
        phrase_list.append(phrase5)
        
        return phrase_list

    def get_random_phrase(self):
        return self.phrases.pop(random.randrange(len(self.phrases)))

    def welcome(self):
        print("========================\n")
        print("Welcome to Phrase Hunter\n")
        print("========================\n")

    def get_guess(self):
        guess = input("Enter a letter: ")
        while True:
            if len(guess) > 1:
                print("Only Input 1 character please!\n")
                guess = input("Enter a letter: \n")
                continue
            elif not self.check_guess(guess):
                print("Input must be a character!\n")
                guess = input("Enter a letter: \n")
                continue
            else:
                break
        return guess

    def check_guess(self,guess):
        if guess.isalpha():
            return True
        elif guess.isdigit():
            return False
        else:
            return False

    
    def start(self):
        self.welcome()
        while(self.missed < 5 and not self.active_phrase.check_complete(self.guesses)):
            print(f'Number missed: {self.missed}')
            user_guess = self.get_guess()
            # print(user_guess)
            self.guesses.append(user_guess)
            self.active_phrase.display(self.guesses)
            if not self.active_phrase.check_guess(user_guess):
                self.missed += 1
        self.game_over()

    def game_over(self):
        if self.missed == 5:
            print("Unfortunately, you have lost the game :(\n")
        else:
            print("Congrats! You have won! :)\n")
        play_again = input("Would you like to play again?  y/n  ")
        if play_again.lower() == 'y':
            self.reset_game()
            self.start()
        else:
            print("Thanks for playing!")

    def reset_game(self):
        self.missed = 0
        self.guesses = [" "]
        self.active_phrase = self.get_random_phrase()
        self.phrases = self.create_phrases()


        



