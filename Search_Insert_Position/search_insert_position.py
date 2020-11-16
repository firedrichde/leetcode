class Solution(object):
    def searchInsertPosition(self, nums: list, target: int) -> int:
        nums_len = len(nums)
        ret = -1
        if nums_len ==0 or target < nums[0]:
            ret = 0
        elif target > nums[nums_len-1]:
            ret = nums_len
        else:
            low = 0
            high = nums_len-1
            while low<=high:
                mid = (int)((low+high)/2)
                if target == nums[mid]:
                    ret = mid
                    return ret
                elif target > nums[mid]:
                    low = mid+1
                else:
                    high = mid-1
            ret = low
            return ret
        


if __name__ == "__main__":
    nums = [1,3,5,6]
    sol = Solution()
    target = 2
    expect_index=1
    actual_index = sol.searchInsertPosition(nums,target)
    assert expect_index == actual_index