class Card:
    def __init__(self, value, suit):
        assert value in Hand.ORDER
        assert suit in Hand.SUITS
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
    
    def getSuits(self):
        return [card.suit for card in self.__cards]
    
    def getCounts(self):
        return [self.getValues().count(card.value) for card in self.__cards]
    
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
        if self.ORDER[i:i+5] != self.getValues():
            return -1
        return i+4
    
    def isStraightFlush(self):
        if self.isStraight() == -1 or self.isFlush() == -1:
            return -1
        i = self.ORDER.index(self.__cards[4].value)
        return i
    
    def isRoyalStraightFlush(self):
        if self.ORDER[-5:] != self.getValues() or self.isFlush() == -1:
            return -1
        return self.ORDER.index("A")
    
    def isFlush(self):
        if len(set(self.getSuits())) != 1:
            return -1
        i = self.ORDER.index(self.__cards[4].value)
        return i
    
    def hasPair(self):
        if len(set(self.getValues())) != 4:
            return -1
        i = self.ORDER.index(self.getValues()[self.getCounts().index(2)])
        return i
    
    def hasTwoPairs(self):
        if not (len(set(self.getValues())) == 3 and max(self.getCounts()) == 2):
            return (-1, -1)
        i, j = self.ORDER.index(self.getValues()[1]), \
            self.ORDER.index(self.getValues()[3])
        return i, j
    
    def hasThreeOfAKind(self):
        counts = self.getCounts()
        if max(counts) != 3:
            return -1
        i = self.ORDER.index(self.getValues()[counts.index(3)])
        return i

    def hasFourOfAKind(self):
        counts = self.getCounts()
        if max(counts) != 4:
            return -1
        i = self.ORDER.index(self.getValues()[counts.index(4)])
        return i
    
    def isFullHouse(self):
        counts = self.getCounts()
        if not (sorted(set(counts)) == [2,3]):
            return -1
        i = self.ORDER.index(self.getValues()[counts.index(3)])
        return i 
    
    def getXHighestCard(self, rank=1):
        return self.ORDER.index(self.getValues()[-rank])
    
    def getResults(self):
        return [self.isRoyalStraightFlush(), self.isStraightFlush(), \
                self.hasFourOfAKind(), self.isFullHouse(), self.isFlush(), \
                self.isStraight(), self.hasThreeOfAKind(), self.hasTwoPairs()[0], \
                self.hasTwoPairs()[1], self.hasPair(), self.getXHighestCard(1), \
                self.getXHighestCard(2), self.getXHighestCard(3), \
                self.getXHighestCard(4), self.getXHighestCard(5)]
    
class Table:
    @staticmethod
    def determineWinner(hand1, hand2):
        i = 0
        hand1Results = hand1.getResults()
        hand2Results = hand2.getResults()
        while i < len(hand1Results):
            if hand1Results[i] > hand2Results[i]:
                return 1
            elif hand1Results[i] < hand2Results[i]:
                return 2
            i += 1
        return 0
        
class Problem54:
    def answer(self):
        f = open("../euler/poker.txt", "r")
        p1Winner = 0
        for line in f:
            hand1 = Hand(line[0:14])
            hand2 = Hand(line[15:29])
            if Table.determineWinner(hand1, hand2) == 1:
                p1Winner += 1
        return p1Winner