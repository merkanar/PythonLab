from item import Item
from result import Result, COMPUTER_WINS, USER_WINS, DRAW

#   Rock subclass of Item
class Rock(Item):
    def __init__(self):
        super().__init__("Rock")

    #   override fight method to return the result of fighting against another item
    def fight(self, other):
        if other.name == "Scissors":
            return Result(COMPUTER_WINS, "Scissors loses to rock")
        elif other.name == "Paper":
            return Result(USER_WINS, "Paper wins against rock")
        else:
            return Result(DRAW, "Draw")