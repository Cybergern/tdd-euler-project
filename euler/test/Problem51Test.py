import unittest
from euler import Problem51

class TestProblem51(unittest.TestCase):

    def setUp(self):
        self.problem = Problem51.Problem51()
        pass
    
    def tearDown(self):
        pass
    
    def test_digitReplacementOf1In13ProducesSixPrimes(self):
        self.assertTrue(self.problem.hasPrimeVariations("13", "1", 6))
        
    def test_digitReplacementOf2In29DoesNotProduceSixPrimes(self):
        self.assertFalse(self.problem.hasPrimeVariations("29", "2", 6))
        
    def test_digitReplacementOf0In56003ProducesSevenPrimes(self):
        self.assertTrue(self.problem.hasPrimeVariations("56003", "0", 7))

    def test_digitReplacementOf6In56603DoesNotProduceSevenPrimes(self):
        self.assertFalse(self.problem.hasPrimeVariations("56603", "6", 7))
        
    def test_digitReplacementOfASixDigitNumberShouldProduceEightPrimes(self):
        self.assertEquals(121313, self.problem.answer())
if __name__ == '__main__':
    unittest.main()