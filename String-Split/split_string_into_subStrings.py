class Solution:

    def __init__(self):
        self.max_number = 0
        self.max_subStrings = None

    def maxUniqueSplit(self, s: str) -> int:
        self.split(list(), s, 0)
        return self.max_number

    def split(self, subStrings: list, s: str, start_index: int):
        if len(subStrings) + len(s) - start_index < self.max_number:
            return
        if self.isASolution(subStrings, s, start_index):
            self.processSolution(subStrings, s, start_index)
        candidates = self.generateSplitCandidate(subStrings, s, start_index)
        for candidate in candidates:
            subStrings.append(candidate)
            self.split(subStrings, s, start_index + len(candidate))
            subStrings.pop()

    def isASolution(self, subStrings: list, s: str, start_index: int):
        return start_index == len(s)

    def processSolution(self, subStrings: list, s: str, start_index: int):
        if len(subStrings) > self.max_number:
            self.max_number = len(subStrings)
            self.max_subStrings = [elem for elem in subStrings]

    def generateSplitCandidate(self, subStrings: list, s: str, start_index: int):
        candidates = list()
        for i in range(start_index, len(s)):
            candidate = s[start_index:i+1]
            if candidate not in subStrings:
                candidates.append(candidate)
        return candidates


if __name__ == "__main__":
    test_sol = Solution()
    test_string = "ababccc"
    print(test_sol.maxUniqueSplit(test_string))
    print(test_sol.max_subStrings)
