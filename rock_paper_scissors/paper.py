from item import Item
from result import Result, COMPUTER_WINS, USER_WINS, DRAW


#   Paper subclass of Item
class Paper(Item):
    def __init__(self):
        super().__init__("Paper")

    #   override fight method to return the result of fighting against another item
    def fight(self, other):
        if other.name == "Rock":
            return Result(COMPUTER_WINS, "Rock loses to paper")
        elif other.name == "Scissors":
            return Result(USER_WINS, "Scissors wins against paper")
        else:
            return Result(DRAW, "Draw")
