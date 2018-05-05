import unittest
from euler.Problem59 import Problem59


class TestProblem59(unittest.TestCase):

    def setUp(self):
        self.problem = Problem59()
        pass
    
    def tearDown(self):
        pass
    
    def test_answerShouldBeNonZero(self):
        self.assertEqual(107359, self.problem.answer())


if __name__ == '__main__':
    unittest.main()
