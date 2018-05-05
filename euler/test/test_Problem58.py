import unittest
from euler.Problem58 import Problem58


class TestProblem58(unittest.TestCase):

    def setUp(self):
        self.problem = Problem58()
        pass
    
    def tearDown(self):
        pass
    
    def test_ShouldGenerateProperDiagonalsFor3By3(self):
        self.assertEqual([3, 5, 7, 9], self.problem.get_diagonals_from_spiral_of_size(3))

    def test_ShouldGenerateProperDiagonalsFor5By5(self):
        self.assertEqual([3, 5, 7, 9, 13, 17, 21, 25], self.problem.get_diagonals_from_spiral_of_size(5))

    def test_ShouldGenerateProperDiagonalsFor7By7(self):
        self.assertEqual([3, 5, 7, 9, 13, 17, 21, 25, 31, 37, 43, 49], self.problem.get_diagonals_from_spiral_of_size(7))
        
    def test_ShouldGenerateProperDiagonalsFor7By7usingPreviousResult(self):
        previousdiagonals = self.problem.get_diagonals_from_spiral_of_size(5)
        self.assertEqual([3, 5, 7, 9, 13, 17, 21, 25, 31, 37, 43, 49],
                         self.problem.get_diagonals_from_spiral_of_size(7, previousdiagonals))

    def test_firstFallBelowTenPercentPrimesOccursOnANonZeroSpiralSize(self):
        self.assertEqual(26241, self.problem.answer())


if __name__ == '__main__':
    unittest.main()
