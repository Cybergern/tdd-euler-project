import itertools


class Problem62:
    @staticmethod
    def sort_digits_desc(number):
        digits = [d for d in str(number)]
        return "".join(sorted(digits, reverse=True))

    def find_lowest_cube_with_number_of_cube_permutations(self, n):
        mapping = {}
        possible_answer = []
        digits = 0
        for i in (x**3 for x in itertools.count(1)):
            sorted_digits = self.sort_digits_desc(i)
            if possible_answer and len(sorted_digits) > digits:
                possible_answer = [l for l in possible_answer if len(l) == n]
                if possible_answer:
                    return min(map(min, possible_answer))
            cubes = mapping.setdefault(sorted_digits, [])
            cubes.append(i)
            if len(cubes) == n:
                possible_answer.append(cubes)
                digits = len(sorted_digits)

    def answer(self):
        return self.find_lowest_cube_with_number_of_cube_permutations(5)
