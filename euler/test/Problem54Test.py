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

if __name__ == '__main__':
    unittest.main()