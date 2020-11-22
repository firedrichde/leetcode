class Solution(object):
    """
    docstring
    """
    East = 0
    South = 1
    West = 2
    North = 3
    Directions = 4

    def __init__(self):
        """
        docstring
        """
        self.elemInOrderMap = {}
        self.cols = -1
        self.rows = -1

    def spiralOrder(self, matrix: list) -> list:
        self.rows = len(matrix)
        if self.rows == 0:
            return list()
        elif self.rows == 1:
            return matrix[0]
        else:
            self._clearOrder()
            self.cols = len(matrix[0])
            result = list()
            for i in range(self.rows):
                for j in range(self.cols):
                    self.elemInOrderMap[(i, j)] = False
            pos = [0, 0, Solution.East]
            # result.append(matrix[0][0])
            # self.elemInOrderMap[(0,0)] = True
            while pos is not None:
                result.append(matrix[pos[0]][pos[1]])
                self._setInOrder(pos[0], pos[1])
                pos = self._findNextElemPos(pos[0], pos[1], pos[2])
            return result

    def _clearOrder(self):
        self.elemInOrderMap = {}

    def _isInOrder(self, i, j):
        return self.elemInOrderMap[(i, j)]

    def _setInOrder(self, i, j):
        self.elemInOrderMap[(i, j)] = True

    def _findNextElemPos(self, i, j, current_direction) -> list:
        """
        docstring
        """
        direction = current_direction
        notReachEnd = False
        for count in range(Solution.Directions):
            available = self._directionAvailable(direction, i, j)
            if available:
                notReachEnd = True
                break
            else:
                direction = (direction+1) % Solution.Directions
        # East
        if notReachEnd:
            if direction == Solution.East:
                return [i, j+1, direction]
            elif direction == Solution.South:
                return [i+1, j, direction]
            elif direction == Solution.West:
                return [i, j-1, direction]
            elif direction == Solution.North:
                return [i-1, j, direction]
            else:
                return None
        else:
            return None

    def _directionAvailable(self, direction, i, j):
        if direction == Solution.East:
            return j+1 < self.cols and not self._isInOrder(i, j+1)
        elif direction == Solution.South:
            return i+1 < self.rows and not self._isInOrder(i+1, j)
        elif direction == Solution.West:
            return j-1 >= 0 and not self._isInOrder(i, j-1)
        elif direction == Solution.North:
            return i-1 >= 0 and not self._isInOrder(i-1, j)
        else:
            return false


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    matrix3 = [[1], [2]]
    matrix4 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    sol = Solution()
    order = sol.spiralOrder(matrix)
    order2 = sol.spiralOrder(matrix2)
    order3 = sol.spiralOrder(matrix3)
    order4 = sol.spiralOrder(matrix4)
    print(order)
    print(order2)
    print(order3)
    print(order4)
