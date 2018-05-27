from euler.Utils import NumberProperties
import math


class Problem66:

    @staticmethod
    def find_d_that_gives_max_x(max_d):
        d = [i for i in range(2, max_d + 1) if not NumberProperties.is_square_simple(i)]
        solutions = [Problem66.find_min_solution(x) for x in d]
        max_value = max(solutions)
        max_index = solutions.index(max_value)
        return d[max_index]

    # Algorithm from here: https://crypto.stanford.edu/pbc/notes/ep/pell.html
    @staticmethod
    def find_min_solution(d):
        a = [math.floor(math.sqrt(d))]
        p = 0
        q = 1
        num = [1, a[0]]
        den = [0, 1]
        while num[-1]**2 - d * den[-1]**2 != 1:
            p = a[-1]*q - p
            q = math.floor((d - p ** 2) / q)
            a.append(math.floor((math.floor(math.sqrt(d)) + p) / q))
            num.append(a[-1]*num[-1] + num[-2])
            den.append(a[-1]*den[-1] + den[-2])
        return num[-1]