class Solution(object):
    """
    docstring
    """
    Empty_Str = ''

    def longestCommonPrefix(self, strs: list) -> str:
        if len(strs) == 0:
            return Solution.Empty_Str
        return self.lcpIter(strs, 0, len(strs)-1)

    def lcpIter(self, strs, start_index, end_index):
        """
        docstring
        """
        if start_index == end_index:
            return strs[start_index]
        else:
            mid_index = (start_index+end_index)//2
            left_str = self.lcpIter(strs, start_index, mid_index)
            right_str = self.lcpIter(strs, mid_index+1, end_index)
            common_str = Solution.merge(left_str, right_str)
            return common_str

    @staticmethod
    def merge(left_str: str, right_str: str) -> str:
        """
        find the longest common prefix between left_str and right_str
        """
        if left_str == Solution.Empty_Str or right_str == Solution.Empty_Str:
            return Solution.Empty_Str
        else:
            str_len = min(len(left_str), len(right_str))
            index = 0
            while index < str_len:
                if left_str[index] != right_str[index]:
                    break
                index += 1
            return left_str[0:index]


if __name__ == "__main__":
    test_sol = Solution()
    test_strs = ["flgower", "flow", "flight"]
    expect_prefix = 'fl'
    actual_prefix = test_sol.longestCommonPrefix(test_strs)
    assert expect_prefix == actual_prefix
