class Solution(object):
    """
    You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps.
    In how many distinct ways can you climb to the top?
    """

    def __init__(self):
        self.values = dict()

    def climbStairs(self, n: int) -> int:
        """
        docstring
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif self.containsKey(n):
            return self.getValue(n)
        else:
            value = self.climbStairs(n-1)+self.climbStairs(n-2)
            self.setValue(n, value)
            return value

    def setValue(self, n: int, value: int):
        self.values[n] = value

    def getValue(self, n: int):
        return self.values[n]

    def containsKey(self, n: int):
        for key in self.values.keys():
            if key == n:
                return True
        return False


if __name__ == "__main__":
    test_sol = Solution()
    test_n = 38
    ret = test_sol.climbStairs(test_n)
    print(ret)
