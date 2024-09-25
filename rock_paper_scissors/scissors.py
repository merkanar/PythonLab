from item import Item
from result import Result, COMPUTER_WINS, USER_WINS, DRAW

#   Scissors subclass of Item
class Scissors(Item):
    def __init__(self):
        super().__init__("Scissors")

    #   override fight method to return the result of fighting against another item
    def fight(self, other):
        if other.name == "Rock":
            return Result(USER_WINS, "Rock wins against scissors")
        elif other.name == "Paper":
            return Result(COMPUTER_WINS, "Paper loses to scissors")
        else:
            return Result(DRAW, "Draw")