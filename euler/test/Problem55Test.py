import unittest
from euler import Problem55

class TestProblem55(unittest.TestCase):

    def setUp(self):
        self.problem = Problem55.Problem55()
        pass
    
    def tearDown(self):
        pass
    
    def test_47ShouldBeNotLychrelNumberInOneIteration(self):
        self.assertEquals(1, self.problem.confirmNotLychrelNumber(47))
        
    def test_349ShouldNotLychrelNumberInThreeIterations(self):
        self.assertEquals(3, self.problem.confirmNotLychrelNumber(349))
        
    def test_196ShouldBeALychrelNumber(self):
        self.assertEquals(-1, self.problem.confirmNotLychrelNumber(196))

    def test_totalNumberOfLychrelNumbersBelowTenThousandShouldBeNonzero(self):
        self.assertEquals(249, self.problem.answer())
if __name__ == '__main__':
    unittest.main()