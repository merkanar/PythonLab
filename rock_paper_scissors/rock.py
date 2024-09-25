from item import Item

#   Rock subclass of Item
class Rock(Item):
    def __init__(self):
        super().__init__("Rock")

    #   override fight method to return the result of fighting against another item
    def fight(self, other):
        if other.name == "Scissors":
            return "Scissors loses to rock"
        elif other.name == "Paper":
            return "Paper wins against rock"
        else:
            return "Draw"