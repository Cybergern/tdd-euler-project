import unittest
<<<<<<< HEAD
from euler.Problem62 import Problem62


class TestProblem62(unittest.TestCase):

    def setUp(self):
        self.problem = Problem62()
=======
from euler.Problem61 import Problem61
from euler.Utils import Numbers


class TestProblem61(unittest.TestCase):

    def setUp(self):
        self.problem = Problem61()
>>>>>>> master
        pass
    
    def tearDown(self):
        pass
    
<<<<<<< HEAD
    def test_cube345_digits_can_be_permuted_to_form_exactly_two_other_cubes(self):
        self.assertEqual(41063625, self.problem.find_lowest_cube_with_number_of_cube_permutations(3))

    def test_answerShouldBeNonZero(self):
        self.assertEqual(127035954683, self.problem.find_lowest_cube_with_number_of_cube_permutations(5))

    def test_answerShouldAvoidDigitBug(self):
        self.assertEqual(1000600120008, self.problem.find_lowest_cube_with_number_of_cube_permutations(6))

=======
    def test_generatedTriListShouldStartCorrectly(self):
        self.assertEqual([1035, 1081, 1128, 1176, 1225], self.problem.generate_list_of_length(Numbers.tri, 4)[:5])
    
    def test_generatedSquareListShouldStartCorrectly(self):
        self.assertEqual([1024, 1089, 1156, 1225, 1296], self.problem.generate_list_of_length(Numbers.sqr, 4)[:5])

    def test_generatedPentListShouldStartCorrectly(self):
        self.assertEqual([1001, 1080, 1162, 1247, 1335], self.problem.generate_list_of_length(Numbers.pen, 4)[:5])

    def test_generatedHexListShouldStartCorrectly(self):
        self.assertEqual([1035, 1128, 1225, 1326, 1431], self.problem.generate_list_of_length(Numbers.hex, 4)[:5])

    def test_generatedHepListShouldStartCorrectly(self):
        self.assertEqual([1071, 1177, 1288, 1404, 1525], self.problem.generate_list_of_length(Numbers.hep, 4)[:5])

    def test_generatedOctListShouldStartCorrectly(self):
        self.assertEqual([1045, 1160, 1281, 1408, 1541], self.problem.generate_list_of_length(Numbers.oct, 4)[:5])

    def test_shouldFindThreeFourDigitNumberCycle(self):
        self.assertEqual([8128, 2882, 8281], self.problem.answer_for_three_numbers())

    def test_answerShouldBeNonZero(self):
        self.assertEqual(28684, self.problem.answer())
>>>>>>> master


if __name__ == '__main__':
    unittest.main()
