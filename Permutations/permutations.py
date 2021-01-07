class Solution(object):
    """
    Given an array nums of distinct integers,return all possible
    permutations.you can return the answer in any order.
    """

    def permute(self, nums: list) -> list:
        return self.permute0(nums, 0, len(nums)-1)

    def permute0(self, nums: list, lo: int, hi: int) -> list:
        if lo == hi:
            ret = list()
            elem = list()
            elem.append(nums[lo])
            ret.append(elem)
            return ret
        else:
            preList = self.permute0(nums, lo+1, hi)
            val = nums[lo]
            ret = list()
            for elem in preList:
                index = 0
                while index <= len(elem):
                    tmp = elem.copy()
                    tmp.insert(index, val)
                    ret.append(tmp)
                    index += 1
            return ret


if __name__ == "__main__":
    test_sol = Solution()
    test_nums = [1, 2, 3, 4, 5, 6]
    ret = test_sol.permute(test_nums)
    print(ret)
    print(len(ret))
