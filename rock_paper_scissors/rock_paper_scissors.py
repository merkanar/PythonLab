from random import randint

from items import get_all_items
from result_processor import ResultProcessor


#   RockPaperScissors class to play the game
class RockPaperScissors:
    def __init__(self):
        self.items = get_all_items()
        self.result_processor = ResultProcessor()

    #   play the game
    def play(self):
        while True:
            random_item = self.get_random_item()
            user_input = input("(R)ock, (P)aper, (S)cissors?")
            if user_input == "q":
                print("Thank you for playing, goodbye!")
                break
            selection = self.find_item(user_input)
            if user_input == "" or selection is None:
                print("Invalid selection")
            else:
                self.result_processor.process_result(random_item.fight(selection))

    # find the item with the user input string
    def find_item(self, name):
        return next((item for item in self.items if item.matches(name)), None)

    # get a random item for the computer selection
    def get_random_item(self):
        random_index = randint(0,2)
        return self.items[random_index]



