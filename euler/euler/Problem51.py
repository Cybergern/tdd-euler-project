from euler.Utils import PrimeChecker

class Problem51:
    def hasEqualNumberOfDigits(self, n1, n2):
        return len(str(int(n1))) == len(str(int(n2)))
    
    def hasPrimeVariations(self, number, replaceDigit, primeVariations):
        primeCount = 0
        for i in range(0, 10):
            testNumber = number.replace(replaceDigit, str(i))
            if PrimeChecker.isPrime(int(testNumber)) \
            and self.hasEqualNumberOfDigits(testNumber, number):
                primeCount += 1
        return primeCount == primeVariations
    
    def answer(self):
        for prime in PrimeChecker.primesBelow(1000000):
            if prime > 100000:
                s = str(prime)
                lastDigit = s[5:6]
                if s.count("0") == 3 and self.hasPrimeVariations(s, "0", 8) \
                or s.count("1") == 3 and lastDigit != 1 and self.hasPrimeVariations(s, "1", 8) \
                or s.count("2") == 3 and self.hasPrimeVariations(s, "2", 8):
                    return int(s) 