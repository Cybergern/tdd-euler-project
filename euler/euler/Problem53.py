from math import factorial


class Problem53:
    @staticmethod
    def comb(n, r):
        assert r <= n
        return factorial(n) / (factorial(r) * factorial(n - r))

    def answer(self):
        c = 0
        for n in range(1, 101):
            for r in range(1, n):
                if self.comb(n, r) > 1000000:
                    c += 1
        return c
