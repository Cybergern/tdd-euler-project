import unittest
from euler.Problem65 import Problem65
from fractions import Fraction


class TestProblem65(unittest.TestCase):

    def setUp(self):
        self.problem = Problem65()
        pass
    
    def tearDown(self):
        pass

    def test_3rd_convergence_should_be_8_div_3(self):
        self.assertEqual(Fraction(8, 3), self.problem.e_convergence(0, 3))

    def test_10th_convergence_should_be_1457_div_536(self):
        self.assertEqual(Fraction(1457, 536), self.problem.e_convergence(0, 10))

    def test_answer(self):
        self.assertEqual(272, self.problem.answer())


if __name__ == '__main__':
    unittest.main()
