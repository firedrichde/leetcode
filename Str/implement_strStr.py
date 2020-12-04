class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '':
            return 0
        else:
            ret = -1
            if len(haystack) >= len(needle):
                for i in range(len(haystack)-len(needle)+1):
                    if haystack[i:i+len(needle)] == needle:
                        ret = i
                        break
            return ret
