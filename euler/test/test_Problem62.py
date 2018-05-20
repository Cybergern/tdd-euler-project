import unittest
from euler.Problem62 import Problem62


class TestProblem62(unittest.TestCase):

    def setUp(self):
        self.problem = Problem62()
        pass
    
    def tearDown(self):
        pass
    
    def test_cube345_digits_can_be_permuted_to_form_exactly_two_other_cubes(self):
        self.assertEqual(41063625, self.problem.find_lowest_cube_with_number_of_cube_permutations(3))

    def test_answerShouldBeNonZero(self):
        self.assertEqual(127035954683, self.problem.find_lowest_cube_with_number_of_cube_permutations(5))

    def test_answerShouldAvoidDigitBug(self):
        self.assertEqual(1000600120008, self.problem.find_lowest_cube_with_number_of_cube_permutations(6))


if __name__ == '__main__':
    unittest.main()
