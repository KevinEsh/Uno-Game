from src.models import Game
from src.utils import *

game = Game(["Kevin","Agustin", "Victor"], init_cards=3)
game.generate()

while True:
    player = game.players[game.turn]
    if not any(game.validCard(card) for card in player.cards):
        player.cards.append(game.deck.pop())
        game.nextTurn()
        continue
    print("Top", game.topCard())
    printIndexSelector(player)
    while True:
        index = waitPlayer()
        if validIndex(index, player):
            if index == -1:
                player.cards.append(game.deck.pop())
                game.nextTurn()
                break
            elif game.validCard(player.cards[index]):
                card = player.cards[index]
                card.activate(game)
                player.cards.remove(card)
                game.dump_deck.append(card)
                game.nextTurn()
                break
    if game.uno(player):
        break
