from euler.Utils import Palindrome


class Problem55:
    def confirm_not_lychrel_number(self, number):
        n = number
        for i in range(0, 50):
            if Palindrome.is_palindrome(n + self.reverse(n)):
                return i + 1
            n = n + self.reverse(n)
        return -1

    @staticmethod
    def reverse(number):
        return int(str(number)[::-1])

    def answer(self):
        sum_total = 0
        for i in range(0, 10000):
            if self.confirm_not_lychrel_number(i) == -1:
                sum_total += 1
        return sum_total
