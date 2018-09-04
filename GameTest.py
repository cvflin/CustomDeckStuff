import cardDeck

def main():
    game = cardDeck.CardDeck()
    game.shuffleDeck()
    game.getDeck()
    game.getHand()
    game.drawTop()
    game.getDeck()
    game.getHand()
    return

main()
