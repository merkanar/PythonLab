import sys
from result import Result, COMPUTER_WINS, USER_WINS

class ResultProcessor:
    def __init__(self):
        self.results = {}
        self.limit = 5

    # process the result of the fight. If the user has won or lost, exit the game
    def process_result(self, result: Result):
        if result is None:
            print("Invalid")
        print(result.message)
        count = self.results.get(result.result, 0) + 1
        print(count)
        if count >= self.limit:
            if result.result == COMPUTER_WINS:
                print("YOU LOSE!")
                sys.exit()
            elif result.result == USER_WINS:
                print("YOU WIN!")
        self.results[result.result] = count
