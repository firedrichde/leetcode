class Solution(object):
    """
    my solution to problem "Remove-Element" in leetcode.com
    """

    def removElement(self, nums: list, val: int) -> int:
        """
        docstring
        """
        nums_len = len(nums)
        if nums_len == 0:
            return 0
        i = 0
        j = nums_len - 1
        result = 0
        while i <= j:
            if nums[i] == val:
                tmp = nums[i]
                while j >= 0 and nums[j] == val:
                    j -= 1
                if j < i:
                    break
                nums[i] = nums[j]
                nums[j] = tmp
                j -= 1
            i += 1
            result += 1
        return result


if __name__ == "__main__":
    nums = [3, 2, 2, 3]
    val = 3
    sol = Solution()

    new_len = sol.removElement(nums,val)
    print(new_len)
    for i in range(new_len):
        print(nums[i])
