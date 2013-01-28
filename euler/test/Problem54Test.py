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
        self.assertTrue(hand.isStraight())
        
    def test_shouldBeAbleToDetectANonStraight(self):
        hand = Problem54.Hand("8C 9D JH JS QD")
        self.assertFalse(hand.isStraight())

    def test_shouldBeAbleToDetectARoyalStraight(self):
        hand = Problem54.Hand("TC JD QH KS AD")
        self.assertTrue(hand.isRoyalStraight())

    def test_shouldBeAbleToDetectANonRoyalStraight(self):
        hand = Problem54.Hand("9C TD JH QS KD")
        self.assertFalse(hand.isRoyalStraight())

    def test_shouldBeAbleToDetectAFlush(self):
        hand = Problem54.Hand("9C TC JC QC KC")
        self.assertTrue(hand.isFlush())

    def test_shouldBeAbleToDetectANonFlush(self):
        hand = Problem54.Hand("9S TC JC QC KC")
        self.assertFalse(hand.isFlush())
        
    def test_shouldBeAbleToDetectAPair(self):
        hand = Problem54.Hand("9S TC TH QC KC")
        self.assertTrue(hand.hasPair())

    def test_shouldBeAbleToDetectANonPair(self):
        hand = Problem54.Hand("9S TC TS TH KC")
        self.assertFalse(hand.hasPair())
        
    def test_shouldBeAbleToDetectTwoPairs(self):
        hand = Problem54.Hand("9S TC TS KH KC")
        self.assertTrue(hand.hasTwoPairs())

    def test_shouldBeAbleToDetectANonTwoPairs(self):
        hand = Problem54.Hand("9S 9C TC JH KC")
        self.assertFalse(hand.hasTwoPairs())
        
    def test_shouldBeAbleToDetectThreeOfAKind(self):
        hand = Problem54.Hand("9S TC TS TH KC")
        self.assertTrue(hand.hasThreeOfAKind())

    def test_shouldBeAbleToDetectANonThreeOfAKind(self):
        hand = Problem54.Hand("9S 9C TC TH KC")
        self.assertFalse(hand.hasThreeOfAKind())
        
    def test_shouldBeAbleToDetectFourOfAKind(self):
        hand = Problem54.Hand("9S TC TS TH TD")
        self.assertTrue(hand.hasFourOfAKind())

    def test_shouldBeAbleToDetectANonFourOfAKind(self):
        hand = Problem54.Hand("9S TC TD TH KC")
        self.assertFalse(hand.hasFourOfAKind())
        
    def test_shouldBeAbleToDetectAFullHouse(self):
        hand = Problem54.Hand("9S 9C TS TH TD")
        self.assertTrue(hand.isFullHouse())

    def test_shouldBeAbleToDetectANonFullHouse(self):
        hand = Problem54.Hand("9S TC TD TH JC")
        self.assertFalse(hand.isFullHouse())
        
    def test_shouldBeAbleToFindHighestCard(self):
        hand = Problem54.Hand("9S TC TD TH JC")
        self.assertEquals("J", hand.getXHighestCard())
        
    def test_shouldBeAbleToFind2ndHighestCard(self):
        hand = Problem54.Hand("9S TC TD TH JC")
        self.assertEquals("T", hand.getXHighestCard(2))
    
if __name__ == '__main__':
    unittest.main()