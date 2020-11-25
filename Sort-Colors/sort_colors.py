class Solution(object):
    """
    docstring
    """

    def sortColors(self, nums: list) -> None:
        """
        docstring
        """
        nums_len = len(nums)
        if nums_len <= 1:
            pass
        else:
            red = 0
            white = 1
            blue = 2
            counts = {}
            counts[red] = 0
            counts[white] = 0
            counts[blue] = 0
            for i in range(nums_len):
                counts[nums[i]] += 1
            index = 0
            for key in counts.keys():
                for i in range(counts[key]):
                    nums[index] = key
                    index += 
            for i in range(nums_len):
                counts[nums[i]] += 1
            index = 0
            for key in counts.keys():
                for i in range(counts[key]):
            for i in range(nums_len):
                counts[nums[i]] += 1
            index = 0
            for key in counts.keys():
                for i in range(counts[key]):
                    nums[index] = key
                    index += 1
                    nums[index] = key
                    index += 11


if __name__ == "__main__":
    nums = [2, 0, t]
    sol = Solution()
    sol.sortColors(nums)
    print(nums)
