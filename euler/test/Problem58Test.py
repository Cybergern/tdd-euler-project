import unittest
from euler import Problem58

class TestProblem58(unittest.TestCase):

    def setUp(self):
        self.problem = Problem58.Problem58()
        pass
    
    def tearDown(self):
        pass
    
    def test_ShouldGenerateProperDiagonalsFor3By3(self):
        self.assertEquals([3,5,7,9], self.problem.getDiagonalsFromSpiralOfSize(3))

    def test_ShouldGenerateProperDiagonalsFor5By5(self):
        self.assertEquals([3,5,7,9,13,17,21,25], self.problem.getDiagonalsFromSpiralOfSize(5))

    def test_ShouldGenerateProperDiagonalsFor7By7(self):
        self.assertEquals([3,5,7,9,13,17,21,25,31,37,43,49], \
                          self.problem.getDiagonalsFromSpiralOfSize(7))
        
    def test_ShouldGenerateProperDiagonalsFor7By7usingPreviousResult(self):
        previousDiagonals = self.problem.getDiagonalsFromSpiralOfSize(5)
        self.assertEquals([3,5,7,9,13,17,21,25,31,37,43,49], \
                          self.problem.getDiagonalsFromSpiralOfSize(7, previousDiagonals))

    def test_firstFallBelowTenPercentPrimesOccursOnANonZeroSpiralSize(self):
        self.assertEquals(26241, self.problem.answer())

if __name__ == '__main__':
    unittest.main()