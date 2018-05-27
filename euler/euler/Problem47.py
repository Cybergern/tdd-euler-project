from euler.Utils import PrimeChecker


class Problem47:
    def __init__(self):
        self.primeChecker = PrimeChecker()
        self.primeChecker.init_prime_factoring()

    def find_consecutive_prime(self, n):
        i = 1
        while True:
            for j in range(0, n):
                if not len(self.primeChecker.get_unique_prime_factors(i, True)) == n:
                    break
                i += 1
                if j == n - 1:
                    return i - n
            i += 1

    def answer(self):
        return self.find_consecutive_prime(4)
