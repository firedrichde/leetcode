class Solution(object):
    """
    docstring
    """
    Directions = 4
    East = 0
    South = 1
    West = 2
    North = 3

    def generateMatrix(self, n: int) -> list:
        """Given a positive integer n, generate an n x n matrix filled with
        elements from 1 to n2 in spiral order.
        """
        self.n = n
        self.result = list()
        init_value = -1
        for i in range(n):
            tmp = list()
            for j in range(n):
                tmp.append(-1)
            self.result.append(tmp)
        i = 0
        j = 0
        direction = Solution.East
        next_direction = None
        for number in range(1, n*n+1):
            self.result[i][j] = number
            if not self._available(direction, i, j):
                next_direction = (direction+1) % Solution.Directions
                while next_direction != direction:
                    if self._available(next_direction, i, j):
                        break
                    next_direction = (next_direction+1) % Solution.Directions
                if next_direction == direction:
                    break
                else:
                    direction = next_direction
            if direction == Solution.East:
                j += 1
            elif direction == Solution.South:
                i += 1
            elif direction == Solution.West:
                j -= 1
            else:
                i -= 1
        return self.result

    def _isEmpty(self, i: int, j: int) -> bool:
        """if there is a element in the position of the matrix,return False,
        otherwise return True
        """
        return self.result[i][j] == -1

    def _available(self, direction, i, j):
        """if next postion is empty in the matrix on the special direction,return True,otherwise return False
        """
        if direction == Solution.East:
            return j+1 < self.n and self._isEmpty(i, j+1)
        elif direction == Solution.South:
            return i+1 < self.n and self._isEmpty(i+1, j)
        elif direction == Solution.West:
            return j-1 >= 0 and self._isEmpty(i, j-1)
        else:
            return i-1 >= 0 and self._isEmpty(i-1, j)


if __name__ == "__main__":
    sol = Solution()
    n = 4
    matrix = sol.generateMatrix(4)
    print(matrix)
