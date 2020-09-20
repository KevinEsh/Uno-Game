class Player:
    def __init__(self, name, cards):
        self.name = name
        self.cards = cards

    def __str__(self):
        return f"Player(name={self.name}, cards=[Card({len(self.cards)})])"

    def __repr__(self):
        return self.__str__(self)

class PC(Player):
    pass
