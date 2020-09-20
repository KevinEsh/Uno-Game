from src.utils import waitColor
class Card:
    def __init__(self, value, color):
        self.value = value
        self.color = color

    def __str__(self):
        return f"Card(value={self.value},color={self.color})"

    def __repr__(self):
        return self.__str__()

    def activate(self, game):
        pass

class PlusCard(Card):
    def activate(self, game):
        turn = game.nextTurn()
        game.players[turn].cards += game.deck[:int(self.value)]
        game.deck = game.deck[int(self.value):]

class RevertCard(Card):
    def activate(self, game):
        game.reverse = not game.reverse

class WildCard(Card):
    def __init__(self, value, color):
        super().__init__(value, None)

    def activate(self, game):
        self.color = waitColor(game)
        # ? game.nextTurn() #?

class CancelCard(Card):
    def activate(self, game):
        game.nextTurn()
