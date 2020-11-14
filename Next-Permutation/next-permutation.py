class Solution(object):
    """
    docstring
    """

    def nextPermutation(self, nums: list) -> None:
        """
        docstring
        """
        not_highest = self.handle(nums, 0)
        if not not_highest:
            i = 0
            j = len(nums)-1
            while i < j:
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
                i += 1
                j -= 1

    def handle(self, nums: list, start_index) -> bool:
        """
        docstring
        """
        if start_index == len(nums)-1:
            return False
        else:
            first_elem = nums[start_index]
            ret = self.handle(nums, start_index+1)
            if ret == False:
                index = start_index+1
                # get a element that greater than first element but is the least one
                while index <= len(nums)-1:
                    if nums[index] > first_elem:
                        index += 1
                    else:
                        break
                if index == start_index+1:
                    return False
                else:
                    newlist = []
                    newlist.append(nums[index-1])
                    tail = len(nums)-1
                    while tail >= start_index:
                        if tail == index-1:
                            newlist.append(first_elem)
                        else:
                            newlist.append(nums[tail])
                        tail -= 1
                    for i in range(start_index, len(nums)):
                        nums[i] = newlist[i-start_index]
                    return True
            else:
                return True
        pass


if __name__ == "__main__":
    sol = Solution()
    nums = [4, 3, 2, 1]
    sol.nextPermutation(nums)
    expect_nums = [2, 1, 4, 3]
    print(nums)
