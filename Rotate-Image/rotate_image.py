class Solution(object):

    """
    docstring
    """

    def rotate(self, matrix: list) -> None:
        """
        docstring
        """
        edge = len(matrix)
        for i in range(edge//2):
            self.rotate_layout(matrix, i)

    def rotate_layout(self, matrix: list, index: int) -> None:
        edge = len(matrix)
        for i in range(index, edge-1-index):
            tmp = matrix[index][i]
            matrix[index][i] = matrix[edge-1-i][index]
            matrix[edge-1-i][index] = matrix[edge-1-index][edge-1-i]
            matrix[edge-1-index][edge-1-i] = matrix[i][edge-1-index]
            matrix[i][edge-1-index] = tmp

    @staticmethod
    def even(x: int) -> bool:
        """
        docstring
        """
        if x % 2 == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    edge = 5
    x = 1
    m = list()
    for i in range(edge):
        p = list()
        for i in range(edge):
            p.append(x)
            x += 1
        m.append(p)
    print(m)
    sol = Solution()
    for i in range(4):
        sol.rotate(m)
    print(m)
