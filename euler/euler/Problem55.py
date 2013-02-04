from euler import Utils

class Problem55:
    def confirmNotLychrelNumber(self, number):
        n = number
        for i in range(0, 50):
            if Utils.Palindrome.isPalindrome(n + self.reverse(n)):
                return i+1
            n = n + self.reverse(n)
        return -1
    
    def reverse(self, number):
        return int(str(number)[::-1])
    
    def answer(self):
        sumTotal = 0
        for i in range(0, 10000):
            if self.confirmNotLychrelNumber(i) == -1:
                sumTotal += 1
        return sumTotal