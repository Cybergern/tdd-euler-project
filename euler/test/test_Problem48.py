import unittest
from euler.Problem48 import Problem48


class TestProblem48(unittest.TestCase):

    def setUp(self):
        self.problem = Problem48()
        pass

    def tearDown(self):
        pass

    def test_sumOfSelfExponentialNumbersUpTo10ShouldBe10405071317(self):
        self.assertEqual(10405071317, self.problem.sum_of_self_exponential_numbers_up_to(10))

    def test_LastTenDigitsOfSumOfSelfExponentialNumbersUpTo1000ShouldBe9110846700(self):
        self.assertEqual("9110846700", str(self.problem.answer())[-10:])


if __name__ == '__main__':
    unittest.main()
