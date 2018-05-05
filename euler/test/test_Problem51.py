import unittest
from euler.Problem51 import Problem51


class TestProblem51(unittest.TestCase):

    def setUp(self):
        self.problem = Problem51()
        pass

    def tearDown(self):
        pass

    def test_digitReplacementOf1In13ProducesSixPrimes(self):
        self.assertTrue(self.problem.has_prime_variations("13", "1", 6))

    def test_digitReplacementOf2In29DoesNotProduceSixPrimes(self):
        self.assertFalse(self.problem.has_prime_variations("29", "2", 6))

    def test_digitReplacementOf0In56003ProducesSevenPrimes(self):
        self.assertTrue(self.problem.has_prime_variations("56003", "0", 7))

    def test_digitReplacementOf6In56603DoesNotProduceSevenPrimes(self):
        self.assertFalse(self.problem.has_prime_variations("56603", "6", 7))

    def test_digitReplacementOfASixDigitNumberShouldProduceEightPrimes(self):
        self.assertEqual(121313, self.problem.answer())


if __name__ == '__main__':
    unittest.main()
