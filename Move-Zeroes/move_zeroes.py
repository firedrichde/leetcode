class Solution:
    def moveZeroes(self, nums: list) -> None:
        nums_len = len(nums)
        target_value = 0
        ori_index = 0
        index = 0
        while ori_index < nums_len:
            if nums[ori_index] != target_value:
                nums[index] = nums[ori_index]
                index += 1
            ori_index += 1
        if index < nums_len:
            for i in range(index, nums_len):
                nums[i] = 0

if __name__ == "__main__":
    test_sol = Solution()
    test_nums = [0, 1, 0, 3, 12]
    test_sol.moveZeroes(test_nums)
    print(test_nums)
