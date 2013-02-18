from euler.Utils import PrimeChecker

class Problem60:
    def __init__(self, primeLimit):
        self.primeChecker = PrimeChecker()
        self.primeChecker.initPrimeFactoring()
        self.primes = PrimeChecker.primesBelow(primeLimit)
        self.primes.remove(2)
        self.pairs = self.buildPairs(self.primes)
    
    def buildPairs(self, primes):
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
                setA = self.pairs[p1] & self.pairs[p2]
                if len(setA) > 0:
                    for p3 in setA:
                        setB = setA & self.pairs[p3]
                        if len(setB) > 0:
                            for p4 in setB:
                                setC = setB & self.pairs[p4]
                                if len(setC) > 0:
                                    total = sum([p1, p2, p3, p4] + list(setC))
                                    if total < lowest:
                                        lowest = total
        return lowest