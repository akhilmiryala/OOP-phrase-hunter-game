import random

class Game:

    def __init__(self):
        setattr(self,'missed',0)
        setattr(self,'phrases',self.create_phrases())
        setattr(self,'active_phrase',self.get_random_phrase())
        setattr(self,'guesses',[" "])

    def create_phrases(self):
        from phrase import Phrase
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



