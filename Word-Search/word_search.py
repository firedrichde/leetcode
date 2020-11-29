class Solution(object):
    """
    docstring
    """

    def exist(self, board: list, word: str) -> bool:
        """
        Given an m x n board and a word, find if the word exists in the grid.
        The word can be constructed from letters of sequentially adjacent cells, where "adjacent" cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
        """
        if len(word) == 0:
            return False
        rows = len(board)
        if rows == 0:
            return False
        else:
            cols = len(board[0])
            if rows*cols < len(word):
                return False
            else:
                word_index = 0
                for i in range(rows):
                    for j in range(cols):
                        if board[i][j] == word[word_index]:
                            if self._exist_iter(board, i, j, word, word_index):
                                return True
                return False

    def _exist_iter(self, board, row_index, col_index, word, word_index):
        """
        find if the letter which at the specify index of the word in the board
        """
        if word_index == len(word):
            return True
        else:
            if row_index < 0 or row_index >= len(board) or col_index < 0 or col_index >= len(board[0]):
                return False
            elif board[row_index][col_index] != word[word_index]:
                return False
            else:
                replace_letter = '#'
                tmp = board[row_index][col_index]
                board[row_index][col_index] = replace_letter
                isExist = self._exist_iter(
                    board, row_index, col_index+1, word, word_index+1) or self._exist_iter(
                    board, row_index+1, col_index, word, word_index+1) or self._exist_iter(
                    board, row_index, col_index-1, word, word_index+1) or self._exist_iter(
                    board, row_index-1, col_index, word, word_index+1)
                board[row_index][col_index] = tmp
                return isExist


if __name__ == "__main__":
    sol = Solution()
    m = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    print(sol.exist(m, word))
