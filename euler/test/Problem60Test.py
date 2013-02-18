import unittest
from euler import Problem60

class TestProblem60(unittest.TestCase):

    def setUp(self):
        pass
    
    def tearDown(self):
        pass
    
    def test_answerShouldBeNonZero(self):
        self.problem = Problem60.Problem60(10000)
        self.assertEquals(26033, self.problem.answer())
    
if __name__ == '__main__':
    unittest.main()