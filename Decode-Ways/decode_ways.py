class Solution(object):
    """
    From: https://leetcode.com/problems/decode-ways/
    """

    def numDecodings(self, s: str) -> int:
        return self.numDecodings0(s, 0, len(s)-1)

    def numDecodings0(self, s: str, low: int, high: int) -> int:
        if low>high:
            return 1
        elif low == high:
            # no character is mapping to number 0
            if s[low] == '0':
                return 0
            else:
                return 1
        else:
            # 'j' is mapping to number 10,'t' is mapping to number 20
            if high-low == 1 and (s[low] == '0' or s[high] == '0'):
                if s[low] == '0' and s[high] == '0':
                    return 0
                else:
                    return 1
            else:
                mid = (low+high)//2
                # '10' or '20' will be separate on divide operation
                if mid+1 < len(s) and s[mid+1] == '0':
                    mid_decoding_num = self.numDecodings0(s, mid, mid+1)
                    left_decoding_num = self.numDecodings0(s, low, mid-1)
                    right_decoding_num = self.numDecodings0(s, mid+2, high)
                    num = left_decoding_num * right_decoding_num * mid_decoding_num
                    return num
                else:
                    left_decoding_num = self.numDecodings0(s, low, mid)
                    right_decoding_num = self.numDecodings0(s, mid+1, high)
                    num = left_decoding_num*right_decoding_num
                    left_edge_char = s[mid]
                    right_edge_char = s[mid+1]
                    mid_coding = int(left_edge_char+right_edge_char)
                    # if the mid num can be
                    # decoded,increase the ways
                    if mid_coding >= 11 and mid_coding <= 26:
                        num += 1
                    return num


if __name__ == "__main__":
    test_sol = Solution()
    test_s = '111111111111111111111111111111111111111111111'
    print(test_sol.numDecodings(test_s))
