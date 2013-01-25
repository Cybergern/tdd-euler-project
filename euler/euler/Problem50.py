from euler.Utils import PrimeChecker 

class Problem50:
    
    def getLongestSumOfConsecutivePrimesBelow(self, n):
        longestSequenceLength = 0
        longestSum = 0
        primes = PrimeChecker.primesBelow(n)
        for i in range(0, len(primes)):
            for j in range(i+1, len(primes)-1):
                primeSum = sum(primes[i:j])
                if primeSum >= n:
                    break
                if PrimeChecker.isPrime(primeSum) and j - i > longestSequenceLength:
                    longestSequenceLength = j - i
                    longestSum = primeSum
        return longestSequenceLength, longestSum
    
    def answer(self):
        return 0