class Item:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def matches(self, name):
        return self.name.lower().startswith(name.lower())

    def fight(self, other):
        return "Invalid"
