class Problem59:
    @staticmethod
    def print_letter_frequencies(dic):
        total_sum = sum(dic.values())
        for key, value in dic.items():
            if value/total_sum*100 > 5:
                print("[" + key + ":" + str(value/total_sum*100) + "%]")

    @staticmethod
    def answer():
        f = open("../resources/cipher1_59.txt", "r")
        contents = f.read()
        f.close()
        numbers = contents.replace("\n", "").split(",")
        decoded = []
        for i in range(0, len(numbers)):
            number = numbers[i]
            if i % 3 == 0:
                decoded.append(int(number) ^ 103)
            elif i % 3 == 1:
                decoded.append(int(number) ^ 111)
            elif i % 3 == 2:
                decoded.append(int(number) ^ 100)
        return sum(decoded)
