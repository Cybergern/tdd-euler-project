import unittest
from euler import Problem61
from euler.Utils import Numbers

class TestProblem61(unittest.TestCase):

    def setUp(self):
        self.problem = Problem61.Problem61()
        pass
    
    def tearDown(self):
        pass
    
    def test_generatedTriListShouldStartCorrectly(self):
        self.assertEquals([1035, 1081, 1128, 1176, 1225], 
                          self.problem.generateListOfLength(Numbers.tri, 4)[:5])
    
    def test_generatedSquareListShouldStartCorrectly(self):
        self.assertEquals([1024, 1089, 1156, 1225, 1296], 
                          self.problem.generateListOfLength(Numbers.sqr, 4)[:5])

    def test_generatedPentListShouldStartCorrectly(self):
        self.assertEquals([1001, 1080, 1162, 1247, 1335], 
                          self.problem.generateListOfLength(Numbers.pen, 4)[:5])

    def test_generatedHexListShouldStartCorrectly(self):
        self.assertEquals([1035, 1128, 1225, 1326, 1431], 
                          self.problem.generateListOfLength(Numbers.hex, 4)[:5])

    def test_generatedHepListShouldStartCorrectly(self):
        self.assertEquals([1071, 1177, 1288, 1404, 1525], 
                          self.problem.generateListOfLength(Numbers.hep, 4)[:5])

    def test_generatedOctListShouldStartCorrectly(self):
        self.assertEquals([1045, 1160, 1281, 1408, 1541], 
                          self.problem.generateListOfLength(Numbers.oct, 4)[:5])

    def test_shouldFindThreeFourDigitNumberCycle(self):
        self.assertEquals([8128, 2882, 8281], self.problem.answerForThreeNumbers())

    def test_answerShouldBeNonZero(self):
        self.assertEquals(28684, self.problem.answer())
   
if __name__ == '__main__':
    unittest.main()