from item import Item


class Scissors(Item):
    def __init__(self):
        super().__init__("Scissors")

    def fight(self, other):
        if other.name == "Rock":
            return "Rock wins against scissors"
        elif other.name == "Paper":
            return "Paper loses to scissors"
        else:
            return "Draw"