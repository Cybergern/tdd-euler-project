class Problem63:

    @staticmethod
    def power_equals_digits(number, exponent):
        answer = number**exponent
        return len(str(answer)) == exponent

    @staticmethod
    def answer():
        power_digits = 0
        for i in range(1, 50):
            for j in range(1, 50):
                if Problem63.power_equals_digits(i, j):
                    power_digits += 1
        return power_digits
