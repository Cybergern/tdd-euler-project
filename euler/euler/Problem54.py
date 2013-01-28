class Card:
    def __init__(self, value, suit):
        assert value in ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
        assert suit in ["H","D","C","S"]
        self.__suit = suit
        self.__value = value
        
    @property
    def suit(self):
        return self.__suit
    
    @property
    def value(self):
        return self.__value
    
    def __str__(self):
        return self.value + self.suit
    
    def __repr__(self):
        return self.__str__()

class Hand:
    ORDER = ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
    SUITS = ["H","D","C","S"]
    
    def __init__(self, hand):
        self.__cards = self.stringToHand(hand)
        
    def getValues(self):
        return [card.value for card in self.__cards]
    
    def toString(self):
        cardString = ""
        for card in self.__cards:
            cardString += card.value + card.suit + " "
        return cardString.rstrip()
    
    def stringToHand(self, hand):
        cardList = hand.split(" ")
        cards = []
        for cardString in cardList:
            cards.append(Card(cardString[0], cardString[1]))
        cards = sorted(cards, key=lambda card: ["".join(self.ORDER).index(c) for c in card.value])
        return cards
    
    def isStraight(self):
        i = self.ORDER.index(self.__cards[0].value)
        return self.ORDER[i:i+5] == self.getValues()
    
    def isRoyalStraight(self):
        return self.ORDER[-5:] == self.getValues()

class Problem54:
    def answer(self):
        return 0