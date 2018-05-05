from euler.Utils import PrimeChecker


class Problem49:

    def tri_sequence_is_prime_and_permutation(self, start, step):
        for n in range(0, 3):
            if not PrimeChecker.isPrime(start + n * step):
                return False
        for n in range(0, 3):
            if not self.is_permutation_of(start + n * step, start):
                return False
        return True

    @staticmethod
    def is_permutation_of(number, other_number):
        return sorted(list(str(number))) == sorted(list(str(other_number)))

    def answer(self):
        for i in range(1000, 10000):
            for j in range(2, 5000, 2):
                if i + j + j >= 10000:
                    break
                if self.tri_sequence_is_prime_and_permutation(i, j) and i != 1487:
                    return int(str(i) + str(i + j) + str(i + j + j))
