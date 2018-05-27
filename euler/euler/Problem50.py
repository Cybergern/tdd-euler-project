from euler.Utils import PrimeChecker


class Problem50:

    @staticmethod
    def get_longest_sum_of_consecutive_primes_below(n):
        longest_sequence_length = 0
        longest_sum = 0
        primes = PrimeChecker.primes_below(n)
        for i in range(0, len(primes)):
            for j in range(i + 1, len(primes) - 1):
                prime_sum = sum(primes[i:j])
                if prime_sum >= n:
                    break
                if PrimeChecker.is_prime(prime_sum) and j - i > longest_sequence_length:
                    longest_sequence_length = j - i
                    longest_sum = prime_sum
        return longest_sequence_length, longest_sum

    @staticmethod
    def answer():
        return 0
