class Solution(object):
    """
    docstring
    """

    def groupAnagrams(self, strs: list) -> list:
        """Given an array of strings strs, group the
        anagrams together. You can return the answer in any order.
        An Anagram is a word or phrase formed by rearranging the letters of
        a different word or phrase, typically using all the original
        letters exactly once.
        """
        unique_sets = []
        result = []
        for anagram in strs:
            tmp_set = set([i for i in anagram])
            new_group = True
            for index in range(len(unique_sets)):
                if tmp_set == unique_sets[index]:
                    result[index].append(anagram)
                    new_group = False
                    break
            if new_group:
                unique_sets.append(tmp_set)
                result.append(list())
                result[-1].append(anagram)
        return result


if __name__ == "__main__":
    test_sol = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = test_sol.groupAnagrams(strs)
    print(result)
