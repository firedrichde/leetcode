class Solution(object):
    """
    docstring
    """

    def mySqrt(self, x: int) -> int:
        """
        Given a non-negative integer x, compute and return the square root of 
        x. Since the return type is an integer, the decimal digits are 
        truncated, and only the integer part of the result is returned.
        """
        start_point = 1.0
        y = start_point
        torlence = 0.1
        while abs(x-y*y) > torlence:
            if y*y == x:
                break
            else:
                next_y = (y+x/y)/2
                y = next_y
        result = int(y)
        if (result+1)*(result+1) <= x:
            result += 1
        return result


if __name__ == "__main__":
    x = 8
    sol = Solution()
    y = sol.mySqrt(x)
    print(y)
