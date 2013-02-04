import unittest
from euler import Problem54

class TestProblem54(unittest.TestCase):

    def setUp(self):
        self.problem = Problem54.Problem54()
        pass
    
    def tearDown(self):
        pass
    
    def test_shouldAcceptALegalHandAndBuildAnObjectFromIt(self):
        handString = "5H 5C 6S 7S KD"
        hand = Problem54.Hand(handString)
        self.assertEquals(handString, hand.toString())
        
    def test_shouldSortHandAfterCreatingIt(self):
        hand = Problem54.Hand("KD 6S 7S 5C 5H")
        self.assertEquals("5C 5H 6S 7S KD", hand.toString())
        
    def test_shouldBeAbleToDetectAStraight(self):
        hand = Problem54.Hand("8C 9D TH JS QD")
        self.assertEquals(hand.ORDER.index("Q"), hand.isStraight())
        
    def test_shouldBeAbleToDetectANonStraight(self):
        hand = Problem54.Hand("8C 9D JH JS QD")
        self.assertEquals(-1, hand.isStraight())

    def test_shouldBeAbleToDetectARoyalStraightFlush(self):
        hand = Problem54.Hand("TC JC QC KC AC")
        self.assertEquals(hand.ORDER.index("A"), hand.isRoyalStraightFlush())

    def test_shouldBeAbleToDetectANonRoyalStraight(self):
        hand = Problem54.Hand("TC JC QC KD AC")
        self.assertEquals(-1, hand.isRoyalStraightFlush())

    def test_shouldBeAbleToDetectAFlush(self):
        hand = Problem54.Hand("9C TC JC QC KC")
        self.assertEquals(hand.ORDER.index("K"), hand.isFlush())

    def test_shouldBeAbleToDetectANonFlush(self):
        hand = Problem54.Hand("9S TC JC QC KC")
        self.assertEquals(-1, hand.isFlush())
        
    def test_shouldBeAbleToDetectAPair(self):
        hand = Problem54.Hand("9S TC TH QC KC")
        self.assertEquals(hand.ORDER.index("T"), hand.hasPair())

    def test_shouldBeAbleToDetectANonPair(self):
        hand = Problem54.Hand("9S TC TS TH KC")
        self.assertEquals(-1, hand.hasPair())
        
    def test_shouldBeAbleToDetectTwoPairs(self):
        hand = Problem54.Hand("9S TC TS KH KC")
        self.assertEquals((hand.ORDER.index("T"), hand.ORDER.index("K")), \
                          hand.hasTwoPairs())

    def test_shouldBeAbleToDetectANonTwoPairs(self):
        hand = Problem54.Hand("9S 9C TC JH KC")
        self.assertEquals((-1, -1), hand.hasTwoPairs())
        
    def test_shouldBeAbleToDetectThreeOfAKind(self):
        hand = Problem54.Hand("9S TC TS TH KC")
        self.assertEquals(hand.ORDER.index("T"), hand.hasThreeOfAKind())

    def test_shouldBeAbleToDetectANonThreeOfAKind(self):
        hand = Problem54.Hand("9S 9C TC TH KC")
        self.assertEquals(-1, hand.hasThreeOfAKind())
        
    def test_shouldBeAbleToDetectFourOfAKind(self):
        hand = Problem54.Hand("9S TC TS TH TD")
        self.assertEquals(hand.ORDER.index("T"), hand.hasFourOfAKind())

    def test_shouldBeAbleToDetectANonFourOfAKind(self):
        hand = Problem54.Hand("9S TC TD TH KC")
        self.assertEquals(-1, hand.hasFourOfAKind())
        
    def test_shouldBeAbleToDetectAFullHouse(self):
        hand = Problem54.Hand("9S 9C TS TH TD")
        self.assertEquals(hand.ORDER.index("T"), hand.isFullHouse())

    def test_shouldBeAbleToDetectANonFullHouse(self):
        hand = Problem54.Hand("9S TC TD TH JC")
        self.assertEquals(-1, hand.isFullHouse())
        
    def test_shouldBeAbleToFindHighestCard(self):
        hand = Problem54.Hand("9S TC TD TH JC")
        self.assertEquals(hand.ORDER.index("J"), hand.getXHighestCard())
        
    def test_shouldBeAbleToFind2ndHighestCard(self):
        hand = Problem54.Hand("9S TC TD TH JC")
        self.assertEquals(hand.ORDER.index("T"), hand.getXHighestCard(2))
        
    def test_shouldBeAbleToDetermineWinnerOfHand1(self):
        hand1 = Problem54.Hand("5H 5C 6S 7S KD")
        hand2 = Problem54.Hand("2C 3S 8S 8D TD")
        self.assertEquals(2, Problem54.Table.determineWinner(hand1, hand2))
        
    def test_shouldBeAbleToDetermineWinnerOfHand2(self):
        hand1 = Problem54.Hand("5D 8C 9S JS AC")
        hand2 = Problem54.Hand("2C 5C 7D 8S QH")
        self.assertEquals(1, Problem54.Table.determineWinner(hand1, hand2))
        
    def test_shouldBeAbleToDetermineWinnerOfHand3(self):
        hand1 = Problem54.Hand("2D 9C AS AH AC")
        hand2 = Problem54.Hand("3D 6D 7D TD QD")
        self.assertEquals(2, Problem54.Table.determineWinner(hand1, hand2))
        
    def test_shouldBeAbleToDetermineWinnerOfHand4(self):
        hand1 = Problem54.Hand("4D 6S 9H QH QC")
        hand2 = Problem54.Hand("3D 6D 7H QD QS")
        self.assertEquals(1, Problem54.Table.determineWinner(hand1, hand2))
        
    def test_shouldBeAbleToDetermineWinnerOfHand5(self):
        hand1 = Problem54.Hand("2H 2D 4C 4D 4S")
        hand2 = Problem54.Hand("3C 3D 3S 9S 9D")
        self.assertEquals(1, Problem54.Table.determineWinner(hand1, hand2))
        
    def test_shouldBeAbleToDetermineWinnerOfHand6(self):
        hand1 = Problem54.Hand("2H 2D 4C 4D 9S")
        hand2 = Problem54.Hand("3C 3S 4S 4H 6D")
        self.assertEquals(2, Problem54.Table.determineWinner(hand1, hand2))
        
    def test_shouldBeAbleToDeterminePlayer1WinsInOneThousandHandsToBeNonZero(self):
        self.assertEquals(376, self.problem.answer())
        
if __name__ == '__main__':
    unittest.main()