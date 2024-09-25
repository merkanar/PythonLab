import sys

class ResultProcessor:
    #   limit is the number of times the user can win or lose before the game ends
    def __init__(self, limit):
        self.results = {}
        self.limit = limit

    # process the result of the fight. If the user has won or lost, exit the game
    def process_result(self, result: 'Result'):
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

class Result:
    def __init__(self, result, message):
        self.result = result
        self.message = message

COMPUTER_WINS = 0
USER_WINS = 1
DRAW = 2
