class Solution:
    def __init__(self):
        self.values = list()

    def generateParenthesis(self, n: int) -> list:
        self.backtrack(list(), 0, n*2)
        return self.values

    def backtrack(self, parenthese_list: list, k: int, n: list):
        if (self.isASolution(parenthese_list, k, n)):
            self.processSolution(parenthese_list)
        else:
            candidates = self.generateCandidates(parenthese_list, k, n)
            for candidate in candidates:
                parenthese_list_copy = list()
                for elem in parenthese_list:
                    parenthese_list_copy.append(elem)
                parenthese_list_copy.append(candidate)
                k += 1
                self.backtrack(parenthese_list_copy, k, n)
                k -= 1

    def isASolution(self, parenthese_list: list, k: int, n: int) -> bool:
        return k == n

    def processSolution(self, parenthese_list: list):
        value = ''.join(parenthese_list)
        self.values.append(value)

    def generateCandidates(self, parenthese_list: list, k: int, n) -> list:
        candidates = list()
        left_bracket = '('
        right_bracket = ")"
        if k == 0:
            candidates.append(left_bracket)
        else:
            left_bracket_count = 0
            right_bracket_count = 0
            for bracket in parenthese_list:
                if bracket == left_bracket:
                    left_bracket_count += 1
                else:
                    right_bracket_count += 1
            if left_bracket_count == n/2:
                candidates.append(right_bracket)
            else:
                if left_bracket_count > right_bracket_count:
                    candidates.append(left_bracket)
                    candidates.append(right_bracket)
                else:
                    candidates.append(left_bracket)
        return candidates


if __name__ == "__main__":
    test_sol = Solution()
    test_n = 3
    print(test_sol.generateParenthesis(test_n))
