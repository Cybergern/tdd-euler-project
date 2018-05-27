from euler.Utils import PrimeChecker


class Problem58:
    
    def __init__(self):
        self.primeChecker = PrimeChecker()
        self.primeChecker.init_prime_factoring()

    @staticmethod
    def get_diagonals_from_spiral_of_size(size, diagonals=None):
        counter = 1
        if diagonals is None:
            diagonals = []
            for i in range(0, int((size-1)/2)):
                for _ in range(0, 4):
                    counter += 2 + 2*i
                    diagonals.append(counter)
        else:
            i = int((size-1)/2) - 1
            counter = int(diagonals[-1])
            for _ in range(0, 4):
                counter += 2 + 2*i
                diagonals.append(counter)
        return diagonals
    
    def answer(self):
        size = 1
        ratio = 100
        diagonals = None
        total_primes = 0
        while ratio >= 0.10:
            size += 2
            diagonals = self.get_diagonals_from_spiral_of_size(size, diagonals)
            total = (size-1)/2 * 4 + 1
            total_primes += len([x for x in diagonals[-4:-1] if self.primeChecker.is_prime(x)])
            ratio = total_primes / total
        return size
