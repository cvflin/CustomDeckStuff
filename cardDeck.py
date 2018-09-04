import random
class CardDeck:

    def __init__(self):
        deck = self.newDeck()
        self.mDeck = deck
        self.mHand = []
        return
    
    def newDeck(self):
        cardList = []
        for i in range(4):
            for x in range(13):
                cardString = ""
                cardString += str(x + 1)
                if i == 0:
                    cardString += " Of Hearts"
                elif i == 1:
                    cardString += " Of Diamonds"
                elif i == 2:
                    cardString += " Of Spades"
                elif i == 3:
                    cardString += " Of Clubs"
                cardList.append(cardString)
        for i in range(len(cardList)):
            if cardList[i][1] == "1":
                cardList[i] = "Jack" + cardList[i][2::]
            if cardList[i][1] == "2":
                cardList[i] = "Queen" + cardList[i][2::]
            if cardList[i][1] == "3":
                cardList[i] = "King" + cardList[i][2::]
        return cardList

    def drawTop(self):
        var = 0
        drawCard = self.mDeck[var]
        self.mHand.append(drawCard)
        self.mDeck.pop(var)
        return
    
    def drawRandom(self):
        var = random.randrange(len(self.mDeck))
        drawCard = self.mDeck[var]
        self.mHand.append(drawCard)
        self.mDeck.pop(var)
        return
    

    def getDeck(self):
        print("")
        print("In Your Deck is: ")
        print(self.mDeck)
        print("")
        return

    def getHand(self):
        print("")
        print("In your hand is: ")
        print(self.mHand)
        print("")
        return

    def shuffleDeck(self):
        newDeck = []
        for i in range(len(self.mDeck)):
            var = random.randrange(len(self.mDeck))
            newDeck.append(self.mDeck[var])
            self.mDeck.pop(var)
        self.mDeck = newDeck
        return










    
