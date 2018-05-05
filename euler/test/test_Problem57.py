import unittest
from euler.Problem57 import Problem57
from fractions import Fraction


class TestProblem57(unittest.TestCase):

    def setUp(self):
        self.problem = Problem57()
        pass
    
    def tearDown(self):
        pass
    
    def test_firstIterationShouldBe3by2(self):
        self.assertEqual(Fraction(3,2), self.problem.get_square_root_iteration(1))

    def test_secondIterationShouldBe7by5(self):
        self.assertEqual(Fraction(7,5), self.problem.get_square_root_iteration(2))

    def test_thirdIterationShouldBe17by12(self):
        self.assertEqual(Fraction(17,12), self.problem.get_square_root_iteration(3))

    def test_fourthIterationShouldBe41by29(self):
        self.assertEqual(Fraction(41,29), self.problem.get_square_root_iteration(4))
        
    def test_sumOfBigNumeratorsShouldBeNonZero(self):
        self.assertEqual(153, self.problem.answer())
    

if __name__ == '__main__':
    unittest.main()
