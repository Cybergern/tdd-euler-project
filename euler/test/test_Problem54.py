import unittest
from euler.Problem54 import Problem54, Table, Hand


class TestProblem54(unittest.TestCase):

    def setUp(self):
        self.problem = Problem54()
        pass

    def tearDown(self):
        pass

    def test_shouldAcceptALegalHandAndBuildAnObjectFromIt(self):
        hand_string = "5H 5C 6S 7S KD"
        hand = Hand(hand_string)
        self.assertEqual(hand_string, hand.to_string())

    def test_shouldSortHandAfterCreatingIt(self):
        hand = Hand("KD 6S 7S 5C 5H")
        self.assertEqual("5C 5H 6S 7S KD", hand.to_string())

    def test_shouldBeAbleToDetectAStraight(self):
        hand = Hand("8C 9D TH JS QD")
        self.assertEqual(hand.ORDER.index("Q"), hand.is_straight())

    def test_shouldBeAbleToDetectANonStraight(self):
        hand = Hand("8C 9D JH JS QD")
        self.assertEqual(-1, hand.is_straight())

    def test_shouldBeAbleToDetectARoyalStraightFlush(self):
        hand = Hand("TC JC QC KC AC")
        self.assertEqual(hand.ORDER.index("A"), hand.is_royal_straight_flush())

    def test_shouldBeAbleToDetectANonRoyalStraight(self):
        hand = Hand("TC JC QC KD AC")
        self.assertEqual(-1, hand.is_royal_straight_flush())

    def test_shouldBeAbleToDetectAFlush(self):
        hand = Hand("9C TC JC QC KC")
        self.assertEqual(hand.ORDER.index("K"), hand.is_flush())

    def test_shouldBeAbleToDetectANonFlush(self):
        hand = Hand("9S TC JC QC KC")
        self.assertEqual(-1, hand.is_flush())

    def test_shouldBeAbleToDetectAPair(self):
        hand = Hand("9S TC TH QC KC")
        self.assertEqual(hand.ORDER.index("T"), hand.has_pair())

    def test_shouldBeAbleToDetectANonPair(self):
        hand = Hand("9S TC TS TH KC")
        self.assertEqual(-1, hand.has_pair())

    def test_shouldBeAbleToDetectTwoPairs(self):
        hand = Hand("9S TC TS KH KC")
        self.assertEqual((hand.ORDER.index("T"), hand.ORDER.index("K")), hand.has_two_pairs())

    def test_shouldBeAbleToDetectANonTwoPairs(self):
        hand = Hand("9S 9C TC JH KC")
        self.assertEqual((-1, -1), hand.has_two_pairs())

    def test_shouldBeAbleToDetectThreeOfAKind(self):
        hand = Hand("9S TC TS TH KC")
        self.assertEqual(hand.ORDER.index("T"), hand.has_three_of_a_kind())

    def test_shouldBeAbleToDetectANonThreeOfAKind(self):
        hand = Hand("9S 9C TC TH KC")
        self.assertEqual(-1, hand.has_three_of_a_kind())

    def test_shouldBeAbleToDetectFourOfAKind(self):
        hand = Hand("9S TC TS TH TD")
        self.assertEqual(hand.ORDER.index("T"), hand.has_four_of_a_kind())

    def test_shouldBeAbleToDetectANonFourOfAKind(self):
        hand = Hand("9S TC TD TH KC")
        self.assertEqual(-1, hand.has_four_of_a_kind())

    def test_shouldBeAbleToDetectAFullHouse(self):
        hand = Hand("9S 9C TS TH TD")
        self.assertEqual(hand.ORDER.index("T"), hand.is_full_house())

    def test_shouldBeAbleToDetectANonFullHouse(self):
        hand = Hand("9S TC TD TH JC")
        self.assertEqual(-1, hand.is_full_house())

    def test_shouldBeAbleToFindHighestCard(self):
        hand = Hand("9S TC TD TH JC")
        self.assertEqual(hand.ORDER.index("J"), hand.get_x_highest_card())

    def test_shouldBeAbleToFind2ndHighestCard(self):
        hand = Hand("9S TC TD TH JC")
        self.assertEqual(hand.ORDER.index("T"), hand.get_x_highest_card(2))

    def test_shouldBeAbleToDetermineWinnerOfHand1(self):
        hand1 = Hand("5H 5C 6S 7S KD")
        hand2 = Hand("2C 3S 8S 8D TD")
        self.assertEqual(2, Table.determine_winner(hand1, hand2))

    def test_shouldBeAbleToDetermineWinnerOfHand2(self):
        hand1 = Hand("5D 8C 9S JS AC")
        hand2 = Hand("2C 5C 7D 8S QH")
        self.assertEqual(1, Table.determine_winner(hand1, hand2))

    def test_shouldBeAbleToDetermineWinnerOfHand3(self):
        hand1 = Hand("2D 9C AS AH AC")
        hand2 = Hand("3D 6D 7D TD QD")
        self.assertEqual(2, Table.determine_winner(hand1, hand2))

    def test_shouldBeAbleToDetermineWinnerOfHand4(self):
        hand1 = Hand("4D 6S 9H QH QC")
        hand2 = Hand("3D 6D 7H QD QS")
        self.assertEqual(1, Table.determine_winner(hand1, hand2))

    def test_shouldBeAbleToDetermineWinnerOfHand5(self):
        hand1 = Hand("2H 2D 4C 4D 4S")
        hand2 = Hand("3C 3D 3S 9S 9D")
        self.assertEqual(1, Table.determine_winner(hand1, hand2))

    def test_shouldBeAbleToDetermineWinnerOfHand6(self):
        hand1 = Hand("2H 2D 4C 4D 9S")
        hand2 = Hand("3C 3S 4S 4H 6D")
        self.assertEqual(2, Table.determine_winner(hand1, hand2))

    def test_shouldBeAbleToDeterminePlayer1WinsInOneThousandHandsToBeNonZero(self):
        self.assertEqual(376, self.problem.answer())


if __name__ == '__main__':
    unittest.main()
