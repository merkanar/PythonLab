import sys
from random import randint

from paper import Paper
from rock import Rock
from result import Result, COMPUTER_WINS, USER_WINS
from scissors import Scissors

#   RockPaperScissors class to play the game
class RockPaperScissors:
    def __init__(self):
        self.items = [Rock(), Paper(), Scissors()]

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
                self.process_result(random_item.fight(selection))

    # find the item with the user input string
    def find_item(self, name):
        return next((item for item in self.items if item.matches(name)), None)

    # get a random item for the computer selection
    def get_random_item(self):
        random_index = randint(0,2)
        return self.items[random_index]

    results = {}
    limit = 5

    # process the result of the fight. If the user has won or lost, exit the game
    def process_result(self, result: Result):
        if result is None:
            print("Invalid")
        print(result.message)
        count = self.results.get(result.result, 0) + 1
        if count >= self.limit:
            if result.result == COMPUTER_WINS:
                print("YOU LOSE!")
                sys.exit()
            elif result.result == USER_WINS:
                print("YOU WIN!")
                sys.exit()
        self.results[result.result] = count



