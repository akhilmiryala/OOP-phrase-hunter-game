
class Phrase():
    
    def __init__(self,phrase):
        self.phrase = phrase.lower()

    def display(self,guesses):
        phrase_in_list = self.phrase.split()
        for word in phrase_in_list:
            for letter in word:
                if letter in guesses:
                    print(f'{letter}',end=" ")
                else:
                    print("_",end=" ")
            print(end = " ")
        print("\n")

    def check_guess(self,guess):
        if guess in self.phrase:
            return True 
        else:
            return False

    def check_complete(self,guesses):
        phrase_in_list = self.phrase.split()
        for word in phrase_in_list:
            for letter in word:
                if letter not in guesses:
                    return False
                else:
                    continue
        return True

        

