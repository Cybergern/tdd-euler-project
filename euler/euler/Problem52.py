class Problem52:
    def getDigits(self, n):
        return "".join(sorted(list(str(n))))
    
    def containsSameDigits(self, n, multiples):
        digits = self.getDigits(n)
        i = 2
        while i <= multiples:
            if not digits == self.getDigits(i*n):
                return False
            i += 1 
        return True
    
    def answer(self):
        i = 100
        while True:
            if self.containsSameDigits(i, 6):
                return i
            i += 1
