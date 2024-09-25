from item import Item

#   Paper subclass of Item
class Paper(Item):
    def __init__(self):
        super().__init__("Paper")

    #   override fight method to return the result of fighting against another item
    def fight(self, other):
        if other.name == "Rock":
            return "Rock loses to paper"
        elif other.name == "Scissors":
            return "Scissors wins against paper"
        else:
            return "Draw"
