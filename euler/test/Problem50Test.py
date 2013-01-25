import unittest
from euler import Problem50

class TestProblem50(unittest.TestCase):

    def setUp(self):
        self.problem = Problem50.Problem50()
        pass
    
    def tearDown(self):
        pass
    
    def test_longestSumOfConsecutivePrimesBelow100ShouldBe41(self):
        self.assertEquals((6, 41), self.problem.getLongestSumOfConsecutivePrimesBelow(100))
        
    def test_longestSumOfConsecutivePrimesBelow1000ShouldBe953(self):
        self.assertEquals((21, 953), self.problem.getLongestSumOfConsecutivePrimesBelow(1000))
        
    def test_longestSumOfConsecutivePrimesBelow1000000ShouldBeNonZero(self):
        self.assertEquals(0, self.problem.getLongestSumOfConsecutivePrimesBelow(1000000))
    
if __name__ == '__main__':
    unittest.main()