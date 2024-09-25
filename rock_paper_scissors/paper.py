from item import Item


class Paper(Item):
    def __init__(self):
        super().__init__("Paper")

    def fight(self, other):
        if other.name == "Rock":
            return "Rock loses to paper"
        elif other.name == "Scissors":
            return "Scissors wins against paper"
        else:
            return "Draw"
