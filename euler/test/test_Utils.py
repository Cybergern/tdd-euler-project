import unittest
from euler.Utils import PrimeChecker


class UtilsTest(unittest.TestCase):

    def setUp(self):
        self.primeChecker = PrimeChecker()
        self.primeChecker.initPrimeFactoring()
        pass

    def tearDown(self):
        pass

    def test_47ShouldBeAPrime(self):
        self.assertTrue(PrimeChecker.isPrime(47))

    def test_27ShouldNotBeAPrime(self):
        self.assertFalse(PrimeChecker.isPrime(27))

    def test_primesBelow20ShouldBe235711131719(self):
        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19], PrimeChecker.primesBelow(20))

    def test_primeFactorsFor644ShouldBe22723(self):
        self.assertEqual([2, 2, 7, 23], self.primeChecker.getPrimeFactors(644, True))

    def test_uniquePrimeFactorsFor644ShouldBe2723(self):
        self.assertEqual([2, 7, 23], self.primeChecker.getUniquePrimeFactors(644, True))


if __name__ == '__main__':
    unittest.main()
