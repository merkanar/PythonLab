from item import Item

#   Scissors subclass of Item
class Scissors(Item):
    def __init__(self):
        super().__init__("Scissors")

    #   override fight method to return the result of fighting against another item
    def fight(self, other):
        if other.name == "Rock":
            return "Rock wins against scissors"
        elif other.name == "Paper":
            return "Paper loses to scissors"
        else:
            return "Draw"