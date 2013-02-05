class Problem56:
    def getDigitSum(self, number):
        return sum([int(digit) for digit in str(number)])
    
    def answer(self):
        maxSum = 0
        for i in range(1, 100):
            for j in range(1, 100):
                if self.getDigitSum(i**j) > maxSum:
                    maxSum = self.getDigitSum(i**j)
        return maxSum