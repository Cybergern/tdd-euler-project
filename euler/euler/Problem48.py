class Problem48:
    def sumOfSelfExponentialNumbersUpTo(self, n):
        totalSum = 0
        for i in range(1, n+1):
            totalSum += i**i
        return totalSum
    
    def answer(self):
        return self.sumOfSelfExponentialNumbersUpTo(1000)