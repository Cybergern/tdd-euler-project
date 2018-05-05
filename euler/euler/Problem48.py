class Problem48:
    @staticmethod
    def sum_of_self_exponential_numbers_up_to(n):
        total_sum = 0
        for i in range(1, n+1):
            total_sum += i**i
        return total_sum
    
    def answer(self):
        return self.sum_of_self_exponential_numbers_up_to(1000)
