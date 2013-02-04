import random

class Palindrome:
    @staticmethod
    def isPalindrome(x):
        return str(x) == str(x)[::-1]

class PrimeChecker:
    @staticmethod
    def millerRabinPass(a, s, d, n):
        aToPower = pow(a, d, n)
        if aToPower == 1:
            return True
        for _ in range(s-1):
            if aToPower == n - 1:
                return True
            aToPower = (aToPower * aToPower) % n
        return aToPower == n - 1

    @staticmethod
    def millerRabin(n):
        d = n - 1
        s = 0
        while d % 2 == 0:
            d >>= 1
            s += 1
        
        for _ in range(20):
            a = 0
            while a == 0:
                a = random.randrange(n)
            if not PrimeChecker.millerRabinPass(a, s, d, n):
                return False
        return True
    
    @staticmethod
    def isPrime(n):
        return PrimeChecker.millerRabin(n)
    
    @staticmethod
    def primesBelow(N):
        correction = N % 6 > 1
        N = {0:N, 1:N-1, 2:N+4, 3:N+3, 4:N+2, 5:N+1}[N%6]
        sieve = [True] * (N // 3)
        sieve[0] = False
        for i in range(int(N ** .5) // 3 + 1):
            if sieve[i]:
                k = (3 * i + 1) | 1
                sieve[k*k // 3::2*k] = [False] * ((N//6 - (k*k)//6 - 1)//k + 1)
                sieve[(k*k + 4*k - 2*k*(i%2)) // 3::2*k] = [False] * ((N // 6 - (k*k + 4*k - 2*k*(i%2))//6 - 1) // k + 1)
        return [2, 3] + [(3 * i + 1) | 1 for i in range(1, N//3 - correction) if sieve[i]]
    
    def initPrimeFactoring(self):
        self._smallPrimes = PrimeChecker.primesBelow(10000)

    def getPrimeFactors(self, n, sort=False):
        factors = []
        limit = int(n ** .5) + 1
        for checker in self._smallPrimes:
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
            if PrimeChecker.isPrime(n):
                factors.append(n)
                break
            factor = PrimeChecker.pollard_brent(n)
            factors.extend(self.getPrimeFactors(factor))
            n //= factor
        if sort: 
            factors.sort()

        return factors
    
    def getUniquePrimeFactors(self, n, sort=False):
        return sorted(list(set(self.getPrimeFactors(n, sort))))
    
    @staticmethod
    def pollard_brent(n):
        if n % 2 == 0: return 2
        if n % 3 == 0: return 3
    
        y, c, m = random.randint(1, n-1), random.randint(1, n-1), random.randint(1, n-1)
        g, r, q = 1, 1, 1
        while g == 1:
            x = y
            for _ in range(r):
                y = (pow(y, 2, n) + c) % n
    
            k = 0
            while k < r and g==1:
                ys = y
                for _ in range(min(m, r-k)):
                    y = (pow(y, 2, n) + c) % n
                    q = q * abs(x-y) % n
                g = PrimeChecker.gcd(q, n)
                k += m
            r *= 2
        if g == n:
            while True:
                ys = (pow(ys, 2, n) + c) % n
                g = PrimeChecker.gcd(abs(x - ys), n)
                if g > 1:
                    break
    
        return g
    
    @staticmethod
    def gcd(a, b):
        if a == b: return a
        while b > 0: a, b = b, a % b
        return a