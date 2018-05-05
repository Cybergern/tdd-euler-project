from euler.Utils import Numbers


class Problem61:
    def __init__(self):
        self.triList = self.generate_list_of_length(Numbers.tri, 4)
        self.sqrList = self.generate_list_of_length(Numbers.sqr, 4)
        self.penList = self.generate_list_of_length(Numbers.pen, 4)
        self.hexList = self.generate_list_of_length(Numbers.hex, 4)
        self.hepList = self.generate_list_of_length(Numbers.hep, 4)
        self.octList = self.generate_list_of_length(Numbers.oct, 4)
        self.allLists = [self.triList, self.sqrList, self.penList, self.hexList, self.hepList, self.octList]

    @staticmethod
    def is_in_sets(check_sets, number):
        for s in check_sets:
            if number in s:
                return True
        return False

    @staticmethod
    def generate_list_of_length(function_arg, length):
        result = []
        start_range = int("1".ljust(length, "0"))
        end_range = int("1".ljust(length + 1, "0"))
        i = 1
        curr = function_arg(i)
        while curr < end_range:
            if curr > start_range:
                result.append(int(curr))
            curr = function_arg(i)
            i += 1
        return result

    @staticmethod
    def get_numbers_starting_with(start, look_set):
        return [x for x in look_set if str(x).startswith(start)]

    def check_lists_for(self, lists_to_check, number, solution):
        if len(lists_to_check) == 0:
            if str(solution[-1])[-2:] == str(solution[0])[:2]:
                return solution
            else:
                return None
        for s in lists_to_check:
            matching_nums = self.get_numbers_starting_with(str(number)[-2:], s)
            for i in matching_nums:
                result = self.check_lists_for([x for x in lists_to_check if x != s], i, solution + [i])
                if result is not None:
                    return result

    def answer_for_three_numbers(self):
        for n in self.triList:
            solution = self.check_lists_for([self.sqrList, self.penList], n, [n])
            if solution is not None:
                return solution

    def answer(self):
        for n in self.triList:
            solution = self.check_lists_for([x for x in self.allLists if x != self.triList], n, [n])
            if solution is not None:
                return sum(solution)
