import unittest
from euler.Problem55 import Problem55


class TestProblem55(unittest.TestCase):

    def setUp(self):
        self.problem = Problem55()
        pass
    
    def tearDown(self):
        pass
    
    def test_47ShouldBeNotLychrelNumberInOneIteration(self):
        self.assertEqual(1, self.problem.confirm_not_lychrel_number(47))
        
    def test_349ShouldNotLychrelNumberInThreeIterations(self):
        self.assertEqual(3, self.problem.confirm_not_lychrel_number(349))
        
    def test_196ShouldBeALychrelNumber(self):
        self.assertEqual(-1, self.problem.confirm_not_lychrel_number(196))

    def test_totalNumberOfLychrelNumbersBelowTenThousandShouldBeNonzero(self):
        self.assertEqual(249, self.problem.answer())


if __name__ == '__main__':
    unittest.main()
