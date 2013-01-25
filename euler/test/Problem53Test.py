import unittest
from euler import Problem53

class TestProblem53(unittest.TestCase):

    def setUp(self):
        self.problem = Problem53.Problem53()
        pass
    
    def tearDown(self):
        pass
    
    def test_selectingThreeNumbersFromFiveCanBeDoneInTenWays(self):
        self.assertEquals(10, self.problem.comb(5,3))
        
    def test_selectingTwoNumbersFromThreeCanBeDoneInThreeWays(self):
        self.assertEquals(3, self.problem.comb(3, 2))
        
    def test_theNumberOfCombinationsResultingInMillionPlusCombinationsShouldBeNonzero(self):
        self.assertEquals(4075, self.problem.answer())

if __name__ == '__main__':
    unittest.main()