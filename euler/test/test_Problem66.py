import unittest
from euler.Problem66 import Problem66


class TestProblem66(unittest.TestCase):

    def setUp(self):
        self.problem = Problem66()
        pass
    
    def tearDown(self):
        pass

    def test_largest_x_value_should_be_9_for_max_d_7(self):
        self.assertEqual(5, self.problem.find_d_that_gives_max_x(7))

    def test_answer(self):
        self.assertEqual(661, self.problem.find_d_that_gives_max_x(1000))


if __name__ == '__main__':
    unittest.main()
