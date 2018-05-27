from fractions import Fraction


class Problem65:

    @staticmethod
    def e_convergence(n, limit):
        if n == 0:
            res = 2
        elif (n + 1) % 3 == 0:
            res = 2*((n+1)/3)
        else:
            res = 1
        if n + 1 == limit:
            return Fraction(res)
        else:
            return Fraction(res) + Fraction(1, Problem65.e_convergence(n+1, limit))

    @staticmethod
    def answer():
        numerator = Problem65.e_convergence(0, 100).numerator
        return sum([int(d) for d in str(numerator)])
