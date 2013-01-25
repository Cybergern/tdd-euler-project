import unittest
from euler import Problem47

class TestProblem47(unittest.TestCase):

    def setUp(self):
        self.problem = Problem47.Problem47()
        pass
    
    def tearDown(self):
        pass
    
    def test_firstTwoConsecutiveTwoPrimeFactorNumbersShouldStartWith14(self):
        self.assertEquals(14, self.problem.findConsecutivePrime(2))
        
    def test_firstThreeConsecutiveThreePrimeFactorNumbersShouldStartWith644(self):
        self.assertEquals(644, self.problem.findConsecutivePrime(3))

    def test_firstFourConsecutiveIntegersWithFourDistinctPrimeFactorsShouldBeNonZero(self):
        self.assertEquals(134043, self.problem.answer())

if __name__ == '__main__':
    unittest.main()