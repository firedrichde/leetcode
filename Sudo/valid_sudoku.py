class Solution(object):
    EmptyCell = '.'

    def print(self, board: list):
        board_len = len(board)
        for i in range(board_len):
            string = ''
            for j in range(board_len):
                string += board[i][j]+' '
            print(string)

    def isValidSudoku(self, board: list) -> bool:
        self.print(board)
        board_len = len(board)
        grid_len = board_len // 3
        for i in range(board_len):
            for j in range(board_len):
                elem = board[i][j]
                if elem == Solution.EmptyCell:
                    continue
                else:
                    for index in range(j+1, board_len):
                        if board[i][index] == elem:
                            return False
                    for index in range(i+1, board_len):
                        if board[index][j] == elem:
                            return False
                    grid_border_i = self.getGridborder(i, grid_len)
                    grid_border_j = self.getGridborder(j, grid_len)
                    for grid_i in range(grid_border_i-grid_len, grid_border_i):
                        for grid_j in range(grid_border_j-grid_len, grid_border_j):
                            if grid_i <= i and grid_j <= j:
                                continue
                            if board[grid_i][grid_j] == elem:
                                return False
        return True

    def getGridborder(self, num: int, grid_len: int) -> int:
        return ((num // grid_len)+1)*grid_len


if __name__ == "__main__":
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
                                                                                                                                                                                                          ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    test_sol = Solution()
    print(test_sol.isValidSudoku(board))
