class Solution(object):
    class RepeatedSet(object):
        def __init__(self, letters):
            self.symbols = {}
            for elem in letters:
                if elem in self.symbols.keys():
                    self.symbols[elem] += 1
                else:
                    self.symbols[elem] = 1

        def equals(self, rs):
            return self.symbols == rs.symbols

    def __init__(self):
        self.repeated_sets = []

    def groupAnagrams(self, strs: list) -> list:
        """Given an array of strings strs, group the
        anagrams together. You can return the answer in any order.
        An Anagram is a word or phrase formed by rearranging the letters of
        a different word or phrase, typically using all the original
        letters exactly once.
        """
        result = []
        for anagram in strs:
            tmp_set = self.parse(anagram)
            group_index = self.group(tmp_set)
            if group_index == -1:
                result.append(list())
                result[-1].append(anagram)
            else:
                result[group_index].append(anagram)
        return result

    def parse(self, anagram: str) -> RepeatedSet:
        return self.RepeatedSet(anagram)

    def group(self, item: RepeatedSet) -> int:
        for index in range(len(self.repeated_sets)):
            if item.equals(self.repeated_sets[index]):
                return index
        self.repeated_sets.append(item)
        return -1


if __name__ == "__main__":
    test_sol = Solution()
    # strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    strs = ["ddddddddddg","dgggggggggg"]
    result = test_sol.groupAnagrams(strs)
    print(result)
