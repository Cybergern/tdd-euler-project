import unittest
from euler.Problem50 import Problem50


class TestProblem50(unittest.TestCase):

    def setUp(self):
        self.problem = Problem50()
        pass

    def tearDown(self):
        pass

    def test_longestSumOfConsecutivePrimesBelow100ShouldBe41(self):
        self.assertEqual((6, 41), self.problem.get_longest_sum_of_consecutive_primes_below(100))

    def test_longestSumOfConsecutivePrimesBelow1000ShouldBe953(self):
        self.assertEqual((21, 953), self.problem.get_longest_sum_of_consecutive_primes_below(1000))

    def test_longestSumOfConsecutivePrimesBelow1000000ShouldBeNonZero(self):
        self.assertEqual((543, 997651), self.problem.get_longest_sum_of_consecutive_primes_below(1000000))


if __name__ == '__main__':
    unittest.main()
