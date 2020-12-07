class Solution(object):
    """
    docstring
    """

    def countAndSay(self, n: int) -> str:
        """
        The count-and-say sequence is a sequence of digit
        strings defined by the recursive formula:
            countAndSay(1) = "1"
            countAndSay(n) is the way you would "say" the digit string
            from countAndSay(n-1), which is then converted into a different
            digit string.
        To determine how you "say" a digit string, split it into the
        minimal number of groups so that each group is a contiguous
        section all of the same character. Then for each group, say
        the number of characters, then say the character. To convert
        the saying into a digit string, replace the counts with a number
        and concatenate every saying.
        """
        if n == 1:
            return '1'
        else:
            previous_str = self.countAndSay(n-1)
            current_str = ''
            tmp_char = previous_str[0]
            char_count = 1
            for i in range(1, len(previous_str)):
                if previous_str[i] != tmp_char and char_count > 0:
                    current_str += str(char_count)+tmp_char
                    tmp_char = previous_str[i]
                    char_count = 1
                else:
                    char_count += 1
            current_str += str(char_count)+tmp_char
            return current_str


if __name__ == "__main__":
    test_sol = Solution()
    n = 5
    print(test_sol.countAndSay(n))
