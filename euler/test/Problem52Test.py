import unittest
from euler import Problem52

class TestProblem52(unittest.TestCase):

    def setUp(self):
        self.problem = Problem52.Problem52()
        pass
    
    def tearDown(self):
        pass
    
    def test_125874DoubledDoesContainSameDigits(self):
        self.assertTrue(self.problem.containsSameDigits(125874, 2))

    def test_125873DoubledDoesNotContainSameDigits(self):
        self.assertFalse(self.problem.containsSameDigits(125873, 2))
        
    def test_sixMultiplesAllHaveSameDigits(self):
        self.assertEquals(142857, self.problem.answer())

if __name__ == '__main__':
    unittest.main()