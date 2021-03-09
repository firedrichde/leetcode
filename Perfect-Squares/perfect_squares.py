class Solution:
    def __init__(self):
        self.squares = list()
        self.count = 0

    def numSquares(self, n: int) -> int:
        if n == 1:
            return 1
        self.count = n+1
        self.searchSquare(n, n // 2, list())
        return len(self.squares)

    def searchSquare(self, n: int, limit: int, squares: list) -> None:
        if len(squares) >= self.count:
            return
        if n == 0:
            if len(squares) < self.count:
                self.squares = [s for s in squares]
                self.count = len(squares)
            return
        square_base = self.getSquare(n, limit)
        for i in range(square_base, 0, -1):
            squares.append(i*i)
            self.searchSquare(n-i*i, i, squares)
            squares.pop()

    def getSquare(self, n: int, limit: int) -> int:
        for i in range(limit, 0, -1):
            if i*i <= n:
                return i


if __name__ == "__main__":
    test_sol = Solution()
    test_num = 6255 
    print(test_sol.numSquares(test_num))
