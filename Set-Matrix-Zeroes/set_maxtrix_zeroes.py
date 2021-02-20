class Solution:
    def setZeroes(self, matrix: list) -> None:
        m = len(matrix)
        n = len(matrix[0])
        rows = [False for i in range(m)]
        cols = [False for i in range(n)]
        for i in range(m):
            for j in range(n):
                value = matrix[i][j]
                if value == 0:
                    rows[i] = True
                    cols[j] = True
                    for k in range(j):
                        matrix[i][k] = 0
                    for k in range(i):
                        matrix[k][j] = 0
                else:
                    if rows[i] or cols[j]:
                        matrix[i][j] = 0


if __name__ == "__main__":
    test_sol = Solution()
    test_matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    print(test_matrix)
    test_sol.setZeroes(test_matrix)
    print(test_matrix)
