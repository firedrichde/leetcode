class Solution(object):
    """
    docstring
    """

    def isPalindrome(self, x: int) -> bool:
        """
        docstring
        """
        if x < 0:
            return False
        elif x >= 0 and x < 10:
            return True
        else:
            reverse_x = 0
            y = x
            base = 10
            while y > 0:
                reverse_x = reverse_x * base + y % base
                y = y // 10
            if reverse_x == x:
                return True
            else:
                return False


if __name__ == "__main__":
    sol = Solution()
    x = 1213
    ret = sol.isPalindrome(x)
    print(ret)
