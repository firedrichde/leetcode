class Solution:
    default_list = [-1, -1]
    # assign delta with a small float because elements in nums are integers
    delta = 0.1
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if self.isOuterSide(nums, target):
            return Solution.default_list
        else:
            target_floor = target - Solution.delta
            target_ceiling = target + Solution.delta
            target_position = self.binarySearch(nums, target)
            if nums[target_position] != target:
                return Solution.default_list
            else :
                start_position = self.binarySearch(nums, target_floor)
                end_position = self.binarySearch(nums, target_ceiling) - 1
                return [start_position, end_position] 
        
    def binarySearch(self, nums: list, target: int):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) //2
            if nums[mid] == target:
                return mid 
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low 
    
    def isOuterSide(self, nums: list, target: int):
        if len(nums) == 0:
            return True 
        else:
            if nums[0] > target or nums[-1] < target:
                return True 
            else:
                return False
          
        
