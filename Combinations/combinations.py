class Solution:
    def __init__(self):
        self.values = list()
        self.candidates = list()

    def combination(self, n: int, k: int) -> list:
        for i in range(1,n+1):
            self.candidates.append(i)
        # void useless compare in method 'generateCandidates'
        self.candidates.reverse()
        self.backtrack(list(), n, k, 0)
        return self.values
    
    def backtrack(self,data: list, n: int, k: int, m: int):
        if self.isACombination(data, n, k, m):
            self.processCombination(data, n, k, m)
        else:
            candidates = self.generateCandidates(data, n, k, m)
            for candidate in candidates:
                data.append(candidate)
                self.backtrack(data, n, k, m+1)
                data.pop()
    
    def isACombination(self, data: list, n: int, k: int, m:int):
        return m == k 
 
    def processCombination(self, data: list, n: int, k: int, m: int):
        value = list()
        for elem in data:
            value.append(elem)
        self.values.append(value)

    def generateCandidates(self, data: list, n: int, k: int, m: int):
        candidates = list()
        if m == 0:
            return self.candidates
        for elem in self.candidates:
            # greater than all elements in data
            if elem > data[-1]:
                candidates.append(elem)
            else:
                break
        return candidates
            
    
        

if __name__ == "__main__":
    test_sol = Solution()
    test_n = 4
    test_k = 2
    test_ret = test_sol.combination(test_n, test_k)
    for elem in test_ret:
        print(elem)
