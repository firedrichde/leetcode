class Solution:
    def __init__(self):
        self.values = dict()

    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        # m and n are symmetry
        if (m, n) in self.values:
            return self.values[(m, n)]
        elif (n, m) in self.values:
            return self.values[(n, m)]
        else:
            value = self.uniquePaths(m-1, n)+self.uniquePaths(m, n-1)
            self.values[(m, n)] = value
            return value


if __name__ == "__main__":
    test_sol = Solution()
    print(test_sol.uniquePaths(3, 3))
