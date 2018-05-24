import math


class Problem64:

    # Algorithm taken from https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Algorithm
    @staticmethod
    def find_repeating_sequence_length(s):
        m = 0
        d = 1
        a0 = math.floor(math.sqrt(s))
        a = a0
        period = 0
        while a != 2*a0:
            m = d * a - m
            d = (s - m ** 2) / d
            a = math.floor((math.sqrt(s) + m) / d)
            period += 1
        return period

    @staticmethod
    def answer():
        relevant_numbers = [i for i in range(2, 10001) if math.modf(math.sqrt(i))[0] != 0.0]
        sequences = list(map(lambda x: Problem64.find_repeating_sequence_length(x), relevant_numbers))
        return sum(list(map(lambda x: x % 2, sequences)))
