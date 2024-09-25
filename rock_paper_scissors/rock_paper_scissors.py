from items import find_item, get_random_item
from results import ResultProcessor


#   RockPaperScissors class to play the game
class RockPaperScissors:
    def __init__(self):
        self.result_processor = ResultProcessor(10)

    #   play the game
    def play(self):
        while True:
            random_item = get_random_item()
            user_input = input("(R)ock, (P)aper, (S)cissors?")
            if user_input == "q":
                print("Thank you for playing, goodbye!")
                break
            selection = find_item(user_input)
            if user_input == "" or selection is None:
                print("Invalid selection")
            else:
                self.result_processor.process_result(random_item.fight(selection))



