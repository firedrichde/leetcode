class Solution(object):
    """
    docstring
    """
    MAX_DUPLICATES_NUM = 2

    def removeDuplicates(self, nums: list) -> int:
        nums_len = len(nums)
        if nums_len <= Solution.MAX_DUPLICATES_NUM:
            return nums_len
        max_value = nums[nums_len-1]
        special_value = max_value+1
        count = 1
        base_value = nums[0]
        for i in range(1, nums_len):
            if nums[i] == base_value:
                count += 1
            else:
                count = 1
                base_value = nums[i]
            if count > Solution.MAX_DUPLICATES_NUM:
                nums[i] = special_value
        nums.sort()
        index = 0
        for elem in nums:
            if elem == special_value:
                break
            else:
                index += 1
        return index



if __name__ == "__main__":
    test_nums = [1, 1, 1, 2, 2, 3]
    test_sol = Solution()
    ret = test_sol.removeDuplicates(test_nums)
    print(ret)
    for i in range(ret):
        print(test_nums[i])
