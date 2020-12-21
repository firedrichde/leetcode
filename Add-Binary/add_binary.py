class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == '0':
            return b
        if b == '0':
            return a
        a_decimal = self.binaryToDecimal(a)
        b_decimal = self.binaryToDecimal(b)
        return self.decimalToBinary(a_decimal+b_decimal)

    def binaryToDecimal(self, x: str) -> int:
        value = 0
        for elem in x:
            value = value*2+int(elem)
        return value

    def decimalToBinary(self, x: int) -> int:
        value = ''
        while x > 0:
            tmp = x % 2
            value = str(tmp)+value
            x = x//2
        return value


if __name__ == "__main__":
    a = '11'
    b = '1'
    test_sol = Solution()
    print(test_sol.addBinary(a,b))
