class Solution:
    def fourSum(self, nums: list, target: int) -> list:
        quadruplets = list()
        self.sort(nums)
        nums_len = len(nums)
        for i in range(nums_len-3):
            if 4*nums[i] > target:
                break
            for j in range(i+1, nums_len-2):
                if nums[i] + 3*nums[j] > target:
                    break
                for k in range(j+1, nums_len-1):
                    if nums[i] + nums[j] + 2*nums[k] > target:
                        break
                    value = target - nums[i] - nums[j] - nums[k]
                    target_index = self.binarySearch(nums, k+1, value)
                    if target_index != -1:
                        tmp_list = list()
                        tmp_list.append(nums[i])
                        tmp_list.append(nums[j])
                        tmp_list.append(nums[k])
                        tmp_list.append(nums[target_index])
                        if tmp_list not in quadruplets:
                            quadruplets.append(tmp_list)
        return quadruplets

    def sort(self, nums: list) -> None:
        nums.sort()

    def binarySearch(self, nums: list, start_index: int, target: int) -> int:
        if start_index >= len(nums):
            return -1
        if nums[start_index] > target or nums[-1] < target:
            return -1
        low = start_index
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1
