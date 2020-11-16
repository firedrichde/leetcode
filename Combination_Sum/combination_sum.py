class Solution:
    def combinationSum(self, candidates: list, target: int) -> list:
        candidates.sort()
        return self.combinationSumIter(candidates, target)

    def combinationSumIter(self, candidates: list, target: int) -> list:
        """
        docstring
        """
        if len(candidates) == 1:
            elem = candidates[0]
            if elem > target:
                return list()
            else:
                if target % elem == 0:
                    x = (int)(target / elem)
                    temp_list = list()
                    for i in range(x):
                        temp_list.append(elem)
                    return [temp_list]
                else:
                    return list()
        else:
            first_elem = candidates[0]
            if first_elem > target:
                return list()
            else:
                x = (int)(target/first_elem)
                y = target % first_elem
                ret_list = list()
                current_combination_list = list()
                for i in range(x):
                    left_list = self.combinationSumIter(
                        candidates[1:], target-i*first_elem)
                    for elem in left_list:
                        if i > 0:
                            for j in range(i):
                                elem.append(first_elem)
                        ret_list.append(elem)
                if y == 0:
                    for i in range(x):
                        current_combination_list.append(first_elem)
                    ret_list.append(current_combination_list)
                return ret_list


# if __name__ == "__main__":
#     candidates = [2, 7, 6, 3, 5, 1]
#     target = 9
#     sol = Solution()
#     result = sol.combinationSum(candidates, target)
#     print(result)
#     print("number of combination: %d" % len(result))
