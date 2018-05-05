class Problem56:
    @staticmethod
    def get_digit_sum(number):
        return sum([int(digit) for digit in str(number)])

    def answer(self):
        max_sum = 0
        for i in range(1, 100):
            for j in range(1, 100):
                if self.get_digit_sum(i ** j) > max_sum:
                    max_sum = self.get_digit_sum(i ** j)
        return max_sum
