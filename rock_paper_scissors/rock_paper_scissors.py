from random import randint

from paper import Paper
from rock import Rock
from scissors import Scissors


class RockPaperScissors:
    def __init__(self):
        self.items = [Rock(), Paper(), Scissors()]

    def play(self):
        while True:
            random_item = self.get_random_item()
            selection = self.find_item(input("(R)ock, (P)aper, (S)cissors?"))
            if selection is None:
                print("Invalid selection")
            else:
                result = random_item.fight(selection)
                print(result)

    def find_item(self, name):
        return next((item for item in self.items if item.matches(name)), None)

    def get_random_item(self):
        random_index = randint(0,2)
        return self.items[random_index]
