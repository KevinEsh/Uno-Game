class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color

    def __str__(self):
        return f"Card(value={self.value},color={self.color})"

    def __repr__(self):
        return self.__str__(self)

    def activate(self, game):
        # if not isinstance(game, Game):
        #     raise Exception # todo: definir exception despues
        pass

class PlusCard(Card):
    def __init__(self, value, color):
        super().__init__(value, color)

    def activate(self, game):
        super().activate(game)
        turn = game.nextTurn()
        game.player[turn].cards += game.deck[:int(self.value)]
        game.deck = game.deck[self.value:]

class RevertCard(Card):
    def __init__(self, value, color):
        super().__init__(value, color)

    def activate(self, game):
        super().activate(game)
        game.revert = not game.revert
        game.nextTurn()

class WildCard(Card):
    def __init__(self, value, color):
        super().__init__(value, color)

    def activate(self, game):
        self.color = game.waitColor()
        game.nextTurn()

class CancelCard(Card):
    def __init__(self, value, color):
        super().__init__(value, color)

    def activate(self, game):
        game.nextTurn()

if __name__ == "__main__":
    c = WildCard(10, "blue")
    print(c)