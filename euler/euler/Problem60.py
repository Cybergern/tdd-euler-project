from euler.Utils import PrimeChecker


class Problem60:
    def __init__(self, prime_limit):
        self.primeChecker = PrimeChecker()
        self.primeChecker.initPrimeFactoring()
        self.primes = PrimeChecker.primesBelow(prime_limit)
        self.primes.remove(2)
        self.pairs = self.build_pairs(self.primes)
    
    def build_pairs(self, primes):
        pairs = dict()
        for p1 in primes:
            if p1 == 5:
                continue
            pairs[p1] = set()
            for q in range(primes.index(p1), len(primes)):
                p2 = primes[q]
                if self.primeChecker.isPrime(int(str(p1) + str(p2))) and \
                        self.primeChecker.isPrime(int(str(p2) + str(p1))):
                    pairs[p1].add(p2)
        return pairs
    
    def answer(self):
        lowest = 10000000
        for p1 in self.pairs:
            for p2 in self.pairs[p1]:
                set_a = self.pairs[p1] & self.pairs[p2]
                if len(set_a) > 0:
                    for p3 in set_a:
                        set_b = set_a & self.pairs[p3]
                        if len(set_b) > 0:
                            for p4 in set_b:
                                set_c = set_b & self.pairs[p4]
                                if len(set_c) > 0:
                                    total = sum([p1, p2, p3, p4] + list(set_c))
                                    if total < lowest:
                                        lowest = total
        return lowest
