class Problem52:
    @staticmethod
    def get_digits(n):
        return "".join(sorted(list(str(n))))
    
    def contains_same_digits(self, n, multiples):
        digits = self.get_digits(n)
        i = 2
        while i <= multiples:
            if not digits == self.get_digits(i * n):
                return False
            i += 1 
        return True
    
    def answer(self):
        i = 100
        while True:
            if self.contains_same_digits(i, 6):
                return i
            i += 1
