from euler.Utils import PrimeChecker


class Problem51:
    @staticmethod
    def has_equal_number_of_digits(n1, n2):
        return len(str(int(n1))) == len(str(int(n2)))

    def has_prime_variations(self, number, replace_digit, prime_variations):
        prime_count = 0
        for i in range(0, 10):
            test_number = number.replace(replace_digit, str(i))
            if PrimeChecker.is_prime(int(test_number)) \
                    and self.has_equal_number_of_digits(test_number, number):
                prime_count += 1
        return prime_count == prime_variations

    def answer(self):
        for prime in PrimeChecker.primes_below(1000000):
            if prime > 100000:
                s = str(prime)
                last_digit = s[5:6]
                if s.count("0") == 3 and self.has_prime_variations(s, "0", 8) \
                        or s.count("1") == 3 and last_digit != 1 and self.has_prime_variations(s, "1", 8) \
                        or s.count("2") == 3 and self.has_prime_variations(s, "2", 8):
                    return int(s)
