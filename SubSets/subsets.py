class Solution(object):
    """
    if nums is [1,2,3],than the binary code represent Subset are shown followed
    '001' => {3}
    '011' => {2,3}
    '111' => {1,2,3}
    '000' => {}
    """
    def subsets(self, nums: list) -> list:
        size = pow(2, len(nums))
        result = list()
        nums_len = len(nums)
        for i in range(size):
            elem = self.binaryToList(self.decimalToBinary(i,nums_len), nums)
            result.append(elem)
        return result

    def decimalToBinary(self, x: int, length: int) -> str:
        binary_str = ''
        while x > 0:
            tmp = x % 2
            binary_str = str(tmp)+binary_str
            x = x // 2
        while len(binary_str) < length:
            binary_str = '0'+binary_str
        return binary_str

    def binaryToList(self, code: str, nums: list) -> list:
        result = list()
        for i in range(len(code)):
            if code[i] == '1':
                result.append(nums[i])
        return result


if __name__ == "__main__":
    test_nums = [1, 2, 3]
    test_sol = Solution()
    ret = test_sol.subsets(test_nums)
    print(ret)
