from game import Game

class Phrase(Game):
    
    def __init__(self,phrase):
        Game.__init__(self)
        self.phrase = phrase.lower()

    def display(self,guesses):
        phrase_in_list = self.phrase.split()
        for letter in phrase_in_list:
            if letter in self.guesses:
                print(f'{letter}',end=" ")
            else:
                print("_",end=" ")
        

