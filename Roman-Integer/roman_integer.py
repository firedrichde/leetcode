class Solution(object):
    """
    docstring
    """
    Roman_Map = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
                 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

    def intToRoman(self, num: int) -> str:
        """
        docstring
        """
        roman_str = ''
        for scale in Solution.Roman_Map.keys():
            if num == 0:
                break
            x = num // scale
            if x > 0:
                for i in range(x):
                    roman_str += Solution.Roman_Map[scale]
                num = num % scale
        return roman_str


if __name__ == "__main__":
    sol = Solution()
    nums = 1994
    roman = sol.intToRoman(nums)
    print(roman)
