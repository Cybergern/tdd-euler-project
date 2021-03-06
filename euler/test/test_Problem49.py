import unittest
from euler.Problem49 import Problem49


class TestProblem49(unittest.TestCase):

    def setUp(self):
        self.problem = Problem49()
        pass

    def tearDown(self):
        pass

    def test_1487IsPermutationOf4817(self):
        self.assertTrue(self.problem.is_permutation_of(1487, 4817))

    def test_1489IsNotPermutationOf4817(self):
        self.assertFalse(self.problem.is_permutation_of(1489, 4817))

    def test_increasingSequence1487_4817_8147IsEachPrimeAndPermutation(self):
        self.assertTrue(self.problem.tri_sequence_is_prime_and_permutation(1487, 3330))

    def test_increasingSequence1489_4819_8149IsNotEachPrimeAndPermutation(self):
        self.assertFalse(self.problem.tri_sequence_is_prime_and_permutation(1489, 3330))

    def test_secondFourDigitIncreasingSequenceEachBothPrimeAndPermutationIsNonzero(self):
        self.assertEqual(296962999629, self.problem.answer())


if __name__ == '__main__':
    unittest.main()
