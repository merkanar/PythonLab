
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
    def fight(self, other):
        return "Invalid"
