class Solution(object):
    def letterCombinations(self, digits: str) -> list:
        if digits == '':
            return []
        return self.letterCombinationsIter(digits, len(digits)-1)

    def letterCombinationsIter(self, digits, end_index: int) -> list:
        if end_index == 0:
            return Solution.getLetter(int(digits[0]))
        else:
            num = int(digits[end_index])
            letters = Solution.getLetter(num)
            leftCombinations = self.letterCombinationsIter(digits, end_index-1)
            combinations = []
            for combination in leftCombinations:
                for letter in letters:
                    combinations.append(Solution.insertLetter(
                        letter, combination, len(combination)+1))
            return combinations

    @staticmethod
    def getLetter(num: int) -> list:
        letters = ['a', 'b', 'c',
                   'd', 'e', 'f',
                   'g', 'h', 'i',
                   'j', 'k', 'l',
                   'm', 'n', 'o',
                   'p', 'q', 'r', 's',
                   't', 'u', 'v',
                   'w', 'x', 'y', 'z']
        if num >= 2 and num <= 6:
            index = 3*(num-2)
            return letters[index:index+3]
        elif num == 7:
            return letters[15:19]
        elif num == 8:
            return letters[19:22]
        elif num == 9:
            return letters[22:26]
        else:
            return []

    @staticmethod
    def insertLetter(letter: str, string: str, index: int) -> str:
        """
        docstring
        """
        if index == 0:
            return letter+string
        elif index == len(string):
            return string+letter
        else:
            return string[0:index]+letter+string[index:]


if __name__ == "__main__":
    test_digits = "39"
    test_sol = Solution()
    actual_combination = test_sol.letterCombinations(test_digits)
    print(actual_combination)
