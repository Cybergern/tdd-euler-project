import unittest
from euler import Problem59

class TestProblem59(unittest.TestCase):

    def setUp(self):
        self.problem = Problem59.Problem59()
        pass
    
    def tearDown(self):
        pass
    
    def test_answerShouldBeNonZero(self):
        self.assertEquals(107359, self.problem.answer())
    
if __name__ == '__main__':
    unittest.main()