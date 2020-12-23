class Solution(object):
    """
    From: https://leetcode.com/problems/decode-ways/
    """

    def __init__(self):
        self.map = {}
        self.valid = True

    def numDecodings(self, s: str) -> int:
        self.check(s)
        if self.valid:
            num = self.decodeWay(s, 0)
            return num
        else:
            return 0

    def decodeWay(self, s: str, index: int) -> bool:
        if index in self.map.keys():
            return self.map[index]
        length = len(s)
        # if index reach the lengh, means the way of decoding is right
        if index == length:
            return 1
        # first way of decoding,only decode the single num
        first_decode_way = self.decode(s[index])
        # second way of decoding,decode two nums
        second_decode_way = index + 1 < length and self.decode(s[index:index+2])
        num = 0
        if first_decode_way:
            num += self.decodeWay(s, index+1)
        if second_decode_way:
            num += self.decodeWay(s, index+2)
        self.map[index] = num 
        return num

    def decode(self, num_str: str) -> bool:
        length = len(num_str)
        if length == 1:
            value = int(num_str)
            if value > 0:
                return True
            else:
                return False
        elif length == 2:
            high_bit_num = int(num_str[0])
            low_bit_num = int(num_str[1])
            if high_bit_num == 1:
                return True
            elif high_bit_num == 2:
                return low_bit_num <= 6
            else:
                return False

    # if the coding is valid,set valid flag true,else set false

    def check(self, s: str) -> None:
        if s.startswith('0'):
            self.valid = False
        else:
            for i in range(1, len(s)):
                value = int(s[i])
                pre_value = int(s[i-1])
                if value == 0 and pre_value != 1 and pre_value != 2:
                    self.valid = False
            self.valid = True


if __name__ == "__main__":
    test_sol = Solution()
    test_s = '111111111111111111111111111111111111111111111'
    print(test_sol.numDecodings(test_s))
