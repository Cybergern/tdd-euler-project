from euler.Utils import PrimeChecker

class Problem47:
    def __init__(self):
        self.primeChecker = PrimeChecker()
        self.primeChecker.initPrimeFactoring()
    
    def findConsecutivePrime(self, n):
        i = 1
        while True:
            for j in range(0, n):
                if not len(self.primeChecker.getUniquePrimeFactors(i, True)) == n:
                    break
                i += 1
                if j == n - 1:
                    return i-n
            i += 1
        
    
    def answer(self):
        return self.findConsecutivePrime(4)