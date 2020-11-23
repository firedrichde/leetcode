class Solution(object):
    """
    docstring
    """
    pass

    def maxSubArray(self, nums: list) -> int:
        """
        docstring
        """
        nums_len = len(nums)
        if nums_len == 1:
            return nums[0]
        else:
            max_value = nums[0]
            tmp = 0
            i = 0
            positive_index = -1
            while i < nums_len:
                positive_index = self._findPositiveNumber(nums, i)
                if positive_index == -1:
                    break
                else:
                    i = positive_index
                    j = i
                    k = i
                    while j < nums_len:
                        if nums[j] < 0 and k == i:
                            k = j
                        tmp += nums[j]
                        if tmp > max_value:
                            max_value = tmp
                        j += 1
                    i = k+1
                tmp = 0
            if positive_index == -1 and max_value < 0:
                return self._findMaxNumber(nums)
            return max_value

    def _findPositiveNumber(self, nums: list, start_index: int) -> int:
        """
        find the first positive number
        """
        current_index = start_index
        nums_len = len(nums)
        while current_index < nums_len:
            if nums[current_index] <= 0:
                current_index += 1
            else:
                break
        if current_index == nums_len:
            return -1
        else:
            return current_index

    def _findMaxNumber(self, nums: list) -> int:
        max_value = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > max_value:
                max_value = nums[i]
        return max_value

    def maxSubArrayFast(self, nums: list) -> int:
        low = 0
        high = len(nums)-1
        if (low == high):
            return nums[low]
        mid = (low+high)//2
        left_max_value = self.maxSubArrayFast(nums[0:mid+1])
        right_max_value = self.maxSubArrayFast(nums[mid+1:])
        return self._combination(nums, mid, left_max_value, right_max_value)

    def _combination(self, nums, mid, left_max_value, right_max_value):
        cross_left = nums[mid]
        cross_right = nums[mid+1]
        i = mid
        tmp = 0
        while i >= 0:
            tmp += nums[i]
            if tmp > cross_left:
                cross_left = tmp
            i -= 1
        i = mid+1
        tmp = 0
        while i < len(nums):
            tmp += nums[i]
            if tmp > cross_right:
                cross_right = tmp
            i += 1
        cross_max_value = cross_left+cross_right
        return max(cross_max_value, left_max_value, right_max_value)


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # nums  = [-2,-1]
    sol = Solution()
    max_value = sol.maxSubArrayFast(nums)
    print(max_value)
