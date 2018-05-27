import unittest
from euler.Utils import PrimeChecker


class UtilsTest(unittest.TestCase):

    def setUp(self):
        self.primeChecker = PrimeChecker()
        self.primeChecker.init_prime_factoring()
        pass

    def tearDown(self):
        pass

    def test_47ShouldBeAPrime(self):
        self.assertTrue(PrimeChecker.is_prime(47))

    def test_27ShouldNotBeAPrime(self):
        self.assertFalse(PrimeChecker.is_prime(27))

    def test_primesBelow20ShouldBe235711131719(self):
        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19], PrimeChecker.primes_below(20))

    def test_primeFactorsFor644ShouldBe22723(self):
        self.assertEqual([2, 2, 7, 23], self.primeChecker.get_prime_factors(644, True))

    def test_uniquePrimeFactorsFor644ShouldBe2723(self):
        self.assertEqual([2, 7, 23], self.primeChecker.get_unique_prime_factors(644, True))


if __name__ == '__main__':
    unittest.main()
