import unittest
from euler.Problem61 import Problem61
from euler.Utils import Numbers


class TestProblem61(unittest.TestCase):

    def setUp(self):
        self.problem = Problem61()
        pass
    
    def tearDown(self):
        pass
    
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


if __name__ == '__main__':
    unittest.main()
