class Solution(object):
    def generate(self, numRows: int) -> list:
        pascal_triangle = list()
        first_line_data = list()
        first_line_data.append(1)
        pascal_triangle.append(first_line_data)
        next_line_data = first_line_data
        for i in range(numRows-1):
            next_line_data = self.nextRow(next_line_data)
            pascal_triangle.append(next_line_data)
        return pascal_triangle

    def nextRow(self, data: list) -> list:
        next_row_data = list()
        next_row_data.append(1)
        for i in range(len(data)-1):
            value = data[i] + data[i+1]
            next_row_data.append(value)
        next_row_data.append(1)
        return next_row_data


if __name__ == "__main__":
    test_sol = Solution()
    test_numRows = 5
    pascal_triangle = test_sol.generate(test_numRows)
    print(pascal_triangle)
