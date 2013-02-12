class Problem59:
    def printLetterFrequencies(self, dic):
        totalSum = sum(dic.values())
        for key, value in dic.items():
            if value/totalSum*100 > 5:
                print("[" + key + ":" + str(value/totalSum*100) + "%]")

    
    def answer(self):
        f = open("../euler/cipher1_59.txt", "r")
        contents = f.read()
        numbers = contents.replace("\n", "").split(",")
        decoded = []
        for i in range(0, len(numbers)):
            number = numbers[i]
            if i % 3 == 0:
                decoded.append(int(number)^103)
            elif i % 3 == 1:
                decoded.append(int(number)^111)
            elif i % 3 == 2:
                decoded.append(int(number)^100)
        return sum(decoded)