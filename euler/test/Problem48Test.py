import unittest
from euler import Problem48

class TestProblem48(unittest.TestCase):

    def setUp(self):
        self.problem = Problem48.Problem48()
        pass
    
    def tearDown(self):
        pass
    
    def test_sumOfSelfExponentialNumbersUpTo10ShouldBe10405071317(self):
        self.assertEquals(10405071317, self.problem.sumOfSelfExponentialNumbersUpTo(10))
        
    def test_LastTenDigitsOfSumOfSelfExponentialNumbersUpTo1000ShouldBe9110846700(self):
        self.assertEquals("9110846700", str(self.problem.answer())[-10:])

if __name__ == '__main__':
    unittest.main()