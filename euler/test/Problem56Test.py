import unittest
from euler import Problem56

class TestProblem56(unittest.TestCase):

    def setUp(self):
        self.problem = Problem56.Problem56()
        pass
    
    def tearDown(self):
        pass
    
    def test_12SquaredDigitSumShouldBe9(self):
        self.assertEquals(9, self.problem.getDigitSum(12**2))
    
    def test_10SquaredDigitSumShouldBe1(self):
        self.assertEquals(1, self.problem.getDigitSum(10**2))
        
    def test_3CubedDigitSumShouldBe9(self):
        self.assertEquals(9, self.problem.getDigitSum(3**3))
        
    def test_maxDigitSumBelowOneHundredShouldBeNonZero(self):
        self.assertEquals(972, self.problem.answer())
        
if __name__ == '__main__':
    unittest.main()