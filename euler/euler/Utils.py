import random


class Palindrome:
    @staticmethod
    def is_palindrome(x):
        return str(x) == str(x)[::-1]


class Numbers:
    @staticmethod
    def tri(x):
        return (x*(x+1))/2

    @staticmethod
    def sqr(x):
        return x**2
    
    @staticmethod
    def pen(x):
        return (x*(3*x-1))/2
    
    @staticmethod
    def hex(x):
        return x*(2*x-1)
    
    @staticmethod
    def hep(x):
        return (x*(5*x-3))/2
    
    @staticmethod
    def oct(x):
        return x*(3*x-2)


class PrimeChecker:

    def __init__(self):
        self._small_primes = []

    @staticmethod
    def miller_rabin_pass(a, s, d, n):
        a_to_power = pow(a, d, n)
        if a_to_power == 1:
            return True
        for _ in range(s-1):
            if a_to_power == n - 1:
                return True
            a_to_power = (a_to_power * a_to_power) % n
        return a_to_power == n - 1

    @staticmethod
    def miller_rabin(n):
        d = n - 1
        s = 0
        while d % 2 == 0:
            d >>= 1
            s += 1
        
        for _ in range(20):
            a = 0
            while a == 0:
                a = random.randrange(n)
            if not PrimeChecker.miller_rabin_pass(a, s, d, n):
                return False
        return True
    
    @staticmethod
    def is_prime(n):
        return PrimeChecker.miller_rabin(n)
    
    @staticmethod
    def primes_below(n):
        correction = n % 6 > 1
        n = {0: n, 1: n - 1, 2: n + 4, 3: n + 3, 4: n + 2, 5: n + 1}[n % 6]
        sieve = [True] * (n // 3)
        sieve[0] = False
        for i in range(int(n ** .5) // 3 + 1):
            if sieve[i]:
                k = (3 * i + 1) | 1
                sieve[k*k // 3::2*k] = [False] * ((n // 6 - (k * k) // 6 - 1) // k + 1)
                sieve[(k*k + 4*k - 2*k*(i % 2)) // 3::2*k] = \
                    [False] * ((n // 6 - (k * k + 4 * k - 2 * k * (i % 2)) // 6 - 1) // k + 1)
        return [2, 3] + [(3 * i + 1) | 1 for i in range(1, n // 3 - correction) if sieve[i]]
    
    def init_prime_factoring(self):
        self._small_primes = PrimeChecker.primes_below(10000)

    def get_prime_factors(self, n, sort=False):
        factors = []
        limit = int(n ** .5) + 1
        for checker in self._small_primes:
            if checker > limit: 
                break
            while n % checker == 0:
                factors.append(checker)
                n //= checker
                limit = int(n ** .5) + 1
                if checker > limit: 
                    break
        if n < 2: 
            return factors
        while n > 1:
            if PrimeChecker.is_prime(n):
                factors.append(n)
                break
            factor = PrimeChecker.pollard_brent(n)
            factors.extend(self.get_prime_factors(factor))
            n //= factor
        if sort: 
            factors.sort()

        return factors
    
    def get_unique_prime_factors(self, n, sort=False):
        return sorted(list(set(self.get_prime_factors(n, sort))))
    
    @staticmethod
    def pollard_brent(n):
        if n % 2 == 0:
            return 2
        if n % 3 == 0:
            return 3
    
        y, c, m = random.randint(1, n-1), random.randint(1, n-1), random.randint(1, n-1)
        g, r, q = 1, 1, 1
        ys, x, = 0
        while g == 1:
            x = y
            for _ in range(r):
                y = (pow(y, 2, n) + c) % n
    
            k = 0
            while k < r and g == 1:
                ys = y
                for _ in range(min(m, r-k)):
                    y = (pow(y, 2, n) + c) % n
                    q = q * abs(x-y) % n
                g = NumberProperties.gcd(q, n)
                k += m
            r *= 2
        if g == n:
            while True:
                ys = (pow(ys, 2, n) + c) % n
                g = NumberProperties.gcd(abs(x - ys), n)
                if g > 1:
                    break
    
        return g


class NumberProperties:
    
    @staticmethod
    def gcd(a, b):
        if a == b:
            return a
        while b > 0:
            a, b = b, a % b
        return a

    @staticmethod
    def is_square_complex(n):
        if n < 0:
            return False
        if n == 0:
            return True
        x, y = 1, n
        while x + 1 < y:
            mid = (x+y)//2
            if mid**2 < n:
                x = mid
            else:
                y = mid
        return n == x**2 or n == (x+1)**2

    @staticmethod
    def is_square_simple(n):
        return n**0.5 == int(n**0.5)
