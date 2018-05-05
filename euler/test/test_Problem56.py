import unittest
from euler.Problem56 import Problem56


class TestProblem56(unittest.TestCase):

    def setUp(self):
        self.problem = Problem56()
        pass
    
    def tearDown(self):
        pass
    
    def test_12SquaredDigitSumShouldBe9(self):
        self.assertEqual(9, self.problem.get_digit_sum(12 ** 2))
    
    def test_10SquaredDigitSumShouldBe1(self):
        self.assertEqual(1, self.problem.get_digit_sum(10 ** 2))
        
    def test_3CubedDigitSumShouldBe9(self):
        self.assertEqual(9, self.problem.get_digit_sum(3 ** 3))
        
    def test_maxDigitSumBelowOneHundredShouldBeNonZero(self):
        self.assertEqual(972, self.problem.answer())


if __name__ == '__main__':
    unittest.main()
