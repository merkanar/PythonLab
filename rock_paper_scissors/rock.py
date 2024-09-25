from item import Item


class Rock(Item):
    def __init__(self):
        super().__init__("Rock")

    def fight(self, other):
        if other.name == "Scissors":
            return "Scissors loses to rock"
        elif other.name == "Paper":
            return "Paper wins against rock"
        else:
            return "Draw"