from euler.Utils import Numbers

class Problem61:
    def __init__(self):
        self.triList = self.generateListOfLength(Numbers.tri, 4)
        self.sqrList = self.generateListOfLength(Numbers.sqr, 4)
        self.penList = self.generateListOfLength(Numbers.pen, 4)
        self.hexList = self.generateListOfLength(Numbers.hex, 4)
        self.hepList = self.generateListOfLength(Numbers.hep, 4)
        self.octList = self.generateListOfLength(Numbers.oct, 4)
        self.allLists = [self.triList, self.sqrList, self.penList, self.hexList, self.hepList, \
                            self.octList]
    
    def isInSets(self, checkSets, number):
        for s in checkSets:
            if number in s:
                return True
        return False
    
    def generateListOfLength(self, function, length):
        result = []
        startRange = int("1".ljust(length, "0"))
        endRange = int("1".ljust(length+1, "0"))
        i = 1
        curr = function(i)
        while curr < endRange:
            if curr > startRange:
                result.append(int(curr))
            curr = function(i)
            i += 1
        return result
    
    def getNumbersStartingWith(self, start, lookSet):
        return [x for x in lookSet if str(x).startswith(start)]
    
    def checkListsFor(self, listsToCheck, number, solution):
        if len(listsToCheck) == 0:
            if str(solution[-1])[-2:] == str(solution[0])[:2]:
                return solution
            else:
                return None
        for s in listsToCheck:
            matchingNums = self.getNumbersStartingWith(str(number)[-2:], s)
            for i in matchingNums:
                result = self.checkListsFor([x for x in listsToCheck if x != s], i, \
                                            solution + [i])
                if result != None:
                    return result
             
    def answerForThreeNumbers(self):
        for n in self.triList:
            solution = self.checkListsFor([self.sqrList, self.penList], n, [n]) 
            if solution != None:
                return solution

             
    def answer(self):
        for n in self.triList:
            solution = self.checkListsFor([x for x in self.allLists if x != self.triList], n, [n]) 
            if solution != None:
                return sum(solution)
            