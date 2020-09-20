from random import choice

def printIndexSelector(player):
    print(player)
    for index, card in enumerate(player.cards):
        print(f"\t{index}.", card)
    print("\t-1. draw a card")

def waitPlayer():
    return int(input("> "))

def waitColor(game):
    for index, color in enumerate(game.colors):
        print(f"\t{index}.", color)
    print("\t-1. random")
    while True:
        index = waitPlayer()
        if validColor(index, game):
            if index == -1:
                color = choice(game.colors)
                break
            else:
                color = game.colors[index]
                break
    return color

def validColor(index, game):
    return index >= -1 and index < len(game.colors)

def validIndex(index, player):
    return index >= -1 and index < len(player.cards)
