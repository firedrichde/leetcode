class Solution(object):
    """
    Given an unsorted integer array nums,
    find the smallest missing positive positive number
    """
    pass

    def firstMissingPositive(self, nums: list) -> int:
        lo = 0
        hi = len(nums)-1
        self.quickSort(nums, lo, hi)
        target = 1
        for elem in nums:
            if elem == target:
                target += 1
        return target

    def partition(self, nums: list, lo: int, hi: int):
        """
        docstring
        """

        value = nums[lo]
        loIndex = lo
        hiIndex = hi+1
        while True:
            loIndex += 1
            hiIndex -= 1
            while loIndex <= hi and nums[loIndex] < value:
                loIndex += 1
            while hiIndex >= lo and value < nums[hiIndex]:
                hiIndex -= 1
            if loIndex >= hiIndex:
                break
            else:
                self.exchange(nums, loIndex, hiIndex)
        self.exchange(nums, lo, hiIndex)
        return hiIndex

    def exchange(self, nums: list, i: int, j: int):
        """
        docstring
        """
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    def quickSort(self, nums: list, lo: int, hi: int):
        if lo >= hi:
            return
        partitionIndex = self.partition(nums, lo, hi)
        self.quickSort(nums, lo, partitionIndex-1)
        self.quickSort(nums, partitionIndex+1, hi)


if __name__ == "__main__":
    test_nums = [1, 2, 0,  4, 5]
    test_sol = Solution()
    ret = test_sol.firstMissingPositive(test_nums)
    print(ret)
