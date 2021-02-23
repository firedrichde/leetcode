class Solution:
    def __init__(self):
        self.min_number = None

    def tilingRectangle(self, n: int, m: int) -> int:
        if m == n:
            return 1
        if m > n:
            return self.tilingRectangle(m, n)
        else:
            # one square(edge=m) and other squares(edge=1) tiling the rectangle
            self.min_number = 1 + m*(n-m)
            barStatus = [0 for i in range(n)]
            self.backtrack(barStatus, m, n, 0)
            return self.min_number

    def backtrack(self, barStatus: list, barLimit: int, barNumber: int, squareNumber: int):
        if squareNumber >= self.min_number:
            # useless rectangle tiling
            return
        if self.rectangleFilled(barStatus, barLimit, barNumber):
            if squareNumber < self.min_number:
                self.min_number = squareNumber
            return
        else:
            tile_start_index = self.getTileStartIndex(
                barStatus, barLimit, barNumber)
            valid_max_square_edge = 1
            for i in range(tile_start_index+1, barNumber):
                if barStatus[i] == barStatus[tile_start_index] and barStatus[tile_start_index] + valid_max_square_edge < barLimit:
                    valid_max_square_edge += 1
            for edge in range(valid_max_square_edge, 0, -1):
                for i in range(tile_start_index, tile_start_index+edge):
                    barStatus[i] += edge
                self.backtrack(barStatus, barLimit, barNumber, squareNumber+1)
                for i in range(tile_start_index, tile_start_index+edge):
                    barStatus[i] -= edge

    def rectangleFilled(self, barStatus: list, barLimit: int, barNumber: int):
        for status in barStatus:
            if status != barLimit:
                return False
        return True

    def getTileStartIndex(self, barStatus: list, barLimit: int, barNumber: int):
        minIndex = 0
        for i in range(1, barNumber):
            if barStatus[i] < barStatus[minIndex]:
                minIndex = i
        return minIndex


if __name__ == "__main__":
    test_sol = Solution()
    test_n = 11
    test_m = 13
    print(test_sol.tilingRectangle(test_n, test_m))
