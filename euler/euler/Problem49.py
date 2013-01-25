from euler.Utils import PrimeChecker 

class Problem49:
    
    def triSequenceIsPrimeAndPermutation(self, start, step):
        for n in range(0, 3):
            if not PrimeChecker.isPrime(start+n*step):
                return False
        for n in range(0, 2):
            if not self.isPermutationOf(n, start):
                return False
        return True
    
    def isPermutationOf(self, number, otherNumber):
        return sorted(list(str(number))) == sorted(list(str(otherNumber))) 
    
    def answer(self):
        for i in range(1000, 10000):
            for j in range(2, 5000, 2):
                if i + j + j >= 10000:
                    break
                if self.triSequenceIsPrimeAndPermutation(i, j) and i != 1487:
                    return int(str(i) + str(i+j) + str(i+j+j))