import unittest
from euler.Problem64 import Problem64


class TestProblem64(unittest.TestCase):

    def setUp(self):
        self.problem = Problem64()
        pass
    
    def tearDown(self):
        pass

    def test_sequence_should_be_found(self):
        self.assertEqual(4, self.problem.find_repeating_sequence_length(23))
    
    def test_answer(self):
        self.assertEqual(1322, self.problem.answer())


if __name__ == '__main__':
    unittest.main()
