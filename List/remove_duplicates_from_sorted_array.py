class RemoveDuplicates(object):
    def removeDuplicates(self, nums: list) -> int:
        """
        Given a sorted array nums, remove the duplicates in-place
        such that each element appears only once and
        returns the new length.Do not allocate extra space
        for another array, you must do this by modifying
        the input array in-place with O(1) extra memory.
        """
        nums_len = len(nums)
        if nums_len <= 1:
            return nums_len
        else:
            unique_index = 1
            common_index = 1
            while common_index < nums_len:
                if nums[common_index] == nums[unique_index-1]:
                    common_index += 1
                else:
                    tmp = nums[unique_index]
                    nums[unique_index] = nums[common_index]
                    nums[common_index] = tmp
                    unique_index += 1
                    common_index += 1
            return unique_index


if __name__ == "__main__":
    test_nums = [0, 0, 1, 1, 2, 2, 3, 3]
    test_obj = RemoveDuplicates()
    unique_len = test_obj.removeDuplicates(test_nums)
    assert unique_len == 4
