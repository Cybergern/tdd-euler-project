import unittest
from euler.Problem63 import Problem63


class TestProblem63(unittest.TestCase):

    def setUp(self):
        self.problem = Problem63()
        pass
    
    def tearDown(self):
        pass
    
    def test_exponent_equals_number_of_digits(self):
        self.assertTrue(self.problem.power_equals_digits(7, 5))

    def test_exponent_doesnt_equal_number_of_digits(self):
        self.assertFalse(self.problem.power_equals_digits(6, 7))

    def test_answer(self):
        self.assertEqual(49, self.problem.answer())


if __name__ == '__main__':
    unittest.main()
