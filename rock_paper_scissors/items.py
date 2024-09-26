from random import randint
from results import Result, COMPUTER_WINS, USER_WINS, DRAW

#   base class for all items
class Item:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    #   returns true if the name of the item matches the name passed in
    def matches(self, name):
        return self.name.lower().startswith(name.lower())

    #   base method for fighting, should be overridden by subclasses
    def fight(self, other: 'Item'):
        return None

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

# contains all items and returns random or selected item
class ItemContainer:
    def __init__(self):
        self.items = [Rock(), Paper(), Scissors()]

    # find the item with the user input string
    def find_item(self, name):
        return next((item for item in self.items if item.matches(name)), None)

    # get a random item for the computer selection
    def get_random_item(self):
        random_index = randint(0, 2)
        return self.items[random_index]