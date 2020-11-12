class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        result_lists = []
        for i in range(numRows):
            result_lists.append(list())
        direct = True
        index = -1
        for i in range(len(s)):
            if direct:
                index += 1
                if index == numRows-1:
                    direct = False
            else:
                index -= 1
                if index == 0:
                    direct = True
            result_lists[index].append(s[i])
        result_str = ""
        for elem in result_lists:
            result_str+="".join(elem)
        return result_str


if __name__ == "__main__":
    msg = "PAYPALISHIRING"
    sol = Solution()
    nums = 3
    ret = sol.convert(msg, nums)
    print(ret)
