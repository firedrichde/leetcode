class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip(' ')
        dec_base = 10
        char_nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        max_int = int(pow(2, 31)-1)
        positive = True
        result = 0
        if s == '':
            return result
        else:
            for i in range(len(s)):
                current_char = s[i]
                if current_char == '-' and 0==i:
                    positive = False
                elif current_char == '+' and 0==i:
                    positive = True
                elif current_char in char_nums:
                    result = result*dec_base + int(current_char)
                    if result > max_int:
                        break
                else:
                    break
        if positive:
            if result > max_int:
                return max_int
            else:
                return result
        else:
            if result > max_int:
                return 0-max_int-1
            else:
                return 0-result


if __name__ == "__main__":
    sol = Solution()
    input = ['42', '-42', '4193 with words', 'words and 987', '-91283472332','  -42','+-42']
    expect = [42, -42, 4193, 0, -2147483648,-42, 0]
    for i in range(len(input)):
        x = sol.myAtoi(input[i])
        print(x)
        assert x == expect[i]
