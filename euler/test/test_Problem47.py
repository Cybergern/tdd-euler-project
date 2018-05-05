import unittest
from euler.Problem47 import Problem47


class TestProblem47(unittest.TestCase):

    def setUp(self):
        self.problem = Problem47()
        pass

    def tearDown(self):
        pass

    def test_firstTwoConsecutiveTwoPrimeFactorNumbersShouldStartWith14(self):
        self.assertEqual(14, self.problem.find_consecutive_prime(2))

    def test_firstThreeConsecutiveThreePrimeFactorNumbersShouldStartWith644(self):
        self.assertEqual(644, self.problem.find_consecutive_prime(3))

    def test_firstFourConsecutiveIntegersWithFourDistinctPrimeFactorsShouldBeNonZero(self):
        self.assertEqual(134043, self.problem.answer())


if __name__ == '__main__':
    unittest.main()
