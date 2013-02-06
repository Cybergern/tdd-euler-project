import unittest
from euler import Problem57
from fractions import Fraction

class TestProblem57(unittest.TestCase):

    def setUp(self):
        self.problem = Problem57.Problem57()
        pass
    
    def tearDown(self):
        pass
    
    def test_firstIterationShouldBe3by2(self):
        self.assertEquals(Fraction(3,2), self.problem.getSquareRootIteration(1))

    def test_secondIterationShouldBe7by5(self):
        self.assertEquals(Fraction(7,5), self.problem.getSquareRootIteration(2))

    def test_thirdIterationShouldBe17by12(self):
        self.assertEquals(Fraction(17,12), self.problem.getSquareRootIteration(3))

    def test_fourthIterationShouldBe41by29(self):
        self.assertEquals(Fraction(41,29), self.problem.getSquareRootIteration(4))
        
    def test_sumOfBigNumeratorsShouldBeNonZero(self):
        self.assertEquals(153, self.problem.answer())
    

if __name__ == '__main__':
    unittest.main()