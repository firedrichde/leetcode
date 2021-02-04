
class Solution:
    def __init__(self):
        self.values = dict()
        self.obstacleGrid = None

    def uniquePathsWithObstacles(self, obstacleGrid: list) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        self.obstacleGrid = obstacleGrid
        self.m = len(obstacleGrid)
        self.n = len(obstacleGrid[0])
        if obstacleGrid[self.m-1][self.n-1] == 1:
            return 0
        all_paths = self.uniquePaths(self.m, self.n)
        return all_paths

    def uniquePaths(self, m: int, n: int) -> int:
        if (m, n) in self.values:
            return self.values[(m, n)]
        # only move right
        if m == 1:
            for i in range(self.n-n, self.n):
                if self.obstacleGrid[self.m-m][i] == 1:
                    self.values[(m, n)] = 0
                    return 0
            self.values[(m, n)] = 1
            return 1
        # only move down
        if n == 1:
            for j in range(self.m-m, self.m):
                if self.obstacleGrid[j][self.n-n] == 1:
                    self.values[(m, n)] = 0
                    return 0
            self.values[(m, n)] = 1
            return 1
        else:
            value = 0
            if self.obstacleGrid[self.m-m+1][self.n-n] == 0:
                value += self.uniquePaths(m-1, n)
            if self.obstacleGrid[self.m-m][self.n-n+1] == 0:
                value += self.uniquePaths(m, n-1)
            self.values[(m, n)] = value
            return value


if __name__ == "__main__":
    test_sol = Solution()
    test_grid = [[0,0,0,0,0],[0,0,0,0,1],[0,0,0,1,0],[0,0,0,0,0]]
    print(test_sol.uniquePathsWithObstacles(test_grid))
