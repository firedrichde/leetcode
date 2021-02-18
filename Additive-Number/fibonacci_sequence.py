class Solution:
    def __init__(self):
        self.num = None
        self.flag = False
        self.values = list()

    def splitIntOfFibonacci(self, S: str) -> list:
        num = S
        self.num = num
        self.backtrack(list(), 0, len(num))
        print(self.values)
        return self.values

    def backtrack(self, values: list, k: int, n: int):
        if self.isASolution(values, k, n):
            self.processSolution(values, k, n)
        else:
            candidates = self.generateCandidates(values, k, n)
            for candidate in candidates:
                if self.flag:
                    break
                values.append(candidate)
                self.backtrack(values, k+1, n)
                values.pop()

    def isASolution(self, values: list, k: int, n: int):
        # print("k={0}, values={1}".format(k, values))
        values_len = len(values)
        if self.valuesLength(values)!= n or  values_len < 3:
            return False
        else:
            for i in range(2, values_len):
                if values[i] != values[i-2] + values[i-1]:
                    return False
            return True

    def processSolution(self, values: list, k:int ,n: int):
        for elem in values:
            self.values.append(elem)
        self.flag = True

    def generateCandidates(self, values: list, k: int, n:int):
        start_index = self.valuesLength(values)
        candidates = list()
        for i in range(start_index, n):
            tmp = self.num[start_index: i+1]
            candidate = int(self.num[start_index : i+1])
            if len(tmp) != len(str(candidate)):
                continue
            if k <= 1:
                candidates.append(candidate)
            else: 
                if len(values) == 2 and candidate >= values[-1]:
                    candidates.append(candidate)
                if len(values) > 2 and candidate == values[-1] + values[-2]:
                    candidates.append(candidate)
        return candidates
            
        
    def valuesLength(self, values: list):
        length = 0
        for elem in values:
            length += len(str(elem))
        return length

    def clear(self):
        self.num = None
        self.values = list()
        self.flag = False
        
            
if __name__ == "__main__":
    test_sol = Solution()
    while True:
        test_str =  input(">num: ") 
        test_ret = test_sol.splitIntOfFibonacci(test_str)
        print(test_ret)
        test_sol.clear()
