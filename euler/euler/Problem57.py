from fractions import Fraction


class Problem57:
    @staticmethod
    def get_square_root_iteration(iterations):
        if iterations == 1:
            return Fraction(3, 2)
        n = 2
        for _ in range(1, iterations):
            n = 2 + Fraction(1, n)
        return 1 + Fraction(1, n)
        
    def answer(self):
        big_num_sum = 0
        for i in range(1, 1001):
            fraction = self.get_square_root_iteration(i)
            if len(str(fraction.numerator)) > len(str(fraction.denominator)):
                big_num_sum += 1
        return big_num_sum
