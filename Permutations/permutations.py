from functools import total_ordering


class Solution(object):
    """
    Given an array nums of distinct integers,return all possible
    permutations.you can return the answer in any order.
    """
    @total_ordering
    class Node(object):
        """
        docstring
        """

        def __init__(self, nums: list):
            """
            docstring
            """
            self.nums = nums

        def __eq__(self, other):
            if len(self.nums) != len(other.nums):
                return False
            else:
                length = len(self.nums)
                for i in range(length):
                    if self.nums[i] != other.nums[i]:
                        return False
                return True

        def __lt__(self, other):
            length = len(self.nums)
            for i in range(length):
                if self.nums[i] < other.nums[i]:
                    return True
                elif self.nums[i] == other.nums[i]:
                    continue
                else:
                    return False
            return False

        def __repr__(self):
            return self.nums.__repr__()

        def getNums(self) -> list:
            return self.nums

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

    def permuteUnique(self, nums: list) -> list:
        """
        docstring
        """
        lists = self.permute(nums)
        nodes = list()
        for elem in lists:
            node = self.Node(elem)
            nodes.append(node)
        ret = self.unique(nodes)
        return ret

    def unique(self, nodes: list) -> list:
        sortedNodes = sorted(nodes)
        index = 1
        size = len(sortedNodes)
        ret = list()
        ret.append(sortedNodes[0].getNums())
        while index < size:
            if sortedNodes[index] != sortedNodes[index-1]:
                ret.append(sortedNodes[index].getNums())
            index += 1
        return ret


if __name__ == "__main__":
    test_sol = Solution()
    test_nums = [1, 2, 3, 4, 1, 2]
    ret = test_sol.permuteUnique(test_nums)
    print(ret)
    print(len(ret))
