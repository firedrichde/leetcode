class Solution:

    def isPalindromic(self, s: str) -> bool:
        s_len = len(s)
        low = 0
        high = s_len-1
        while low < high:
            if s[low] != s[high]:
                return False
            low += 1
            high -= 1
        return True

    # time o(n^2) space O(1)
    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        low = 0
        high = 0
        for i in range(s_len):
            if i > 0:
                # palindrome length is even
                if s[i] == s[i-1]:
                    j = 0
                    while i-1-j >= 0 and i+j < s_len and s[i-1-j] == s[i+j]:
                        j += 1
                    if 2*j > high - low + 1:
                        low = i-j
                        high = i+j-1
            if i > 1:
                # palindrome lengh is odd
                if s[i] == s[i-2]:
                    j = 0
                    while i-2-j >= 0 and i+j < s_len and s[i-2-j] == s[i+j]:
                        j += 1
                    if 2*j + 1 > high - low + 1:
                        low = i-1-j
                        high = i+j-1
        return s[low:high+1]

    # mamacher algorithm time O(n) space(n)
    def manacher(self, s: str) -> str:
        s_len = len(s)
        even_distance_list = list()
        odd_distance_list = list()
        left = 0
        right = -1
        # odd palindrome
        for i in range(s_len):
            if i > right:
                distance = 1
                while i-distance >= 0 and i+distance < s_len and s[i-distance] == s[i+distance]:
                    distance += 1
                odd_distance_list.append(distance-1)
            else:
                j = left + right - i
                if i+odd_distance_list[j] < right:
                    odd_distance_list.append(odd_distance_list[j])
                else:
                    odd_distance_list.append(right - i)
                    distance = right - i
                    while i-distance >= 0 and i + distance < s_len and s[i-distance] == s[i+distance]:
                        distance += 1
                    odd_distance_list[i] = distance-1
                    # right = i+odd_distance_list[i]
                    # left = i-odd_distance_list[i]
            if i+odd_distance_list[i] > right:
                right = i+odd_distance_list[i]
                left = i-odd_distance_list[i]

        left = 0
        right = -1 
        # even palindromic
        for i in range(s_len):
            if i > right:
                distance = 0
                while i-1-distance >= 0 and i+distance < s_len and s[i-1-distance] == s[i+distance]:
                    distance += 1
                even_distance_list.append(distance-1)
            else:
                j = left + right - i + 1
                if i+even_distance_list[j] < right:
                    even_distance_list.append(even_distance_list[j])
                else:
                    even_distance_list.append(right-i)
                    distance = right-i
                    while i-1-distance >= 0 and i+distance < s_len and s[i-1-distance] == s[i+distance]:
                        distance += 1
                    even_distance_list[i] = distance-1
            if i+even_distance_list[i] > right:
                right = i+even_distance_list[i]
                left = i-even_distance_list[i]-1

        max_odd_index = 0
        max_even_index = 0
        for i in range(s_len):
            if odd_distance_list[i] > odd_distance_list[max_odd_index]:
                max_odd_index = i
            if even_distance_list[i] > even_distance_list[max_even_index]:
                max_even_index = i
        low = 0
        high = 0
        if odd_distance_list[max_odd_index]*2+1 > (even_distance_list[max_even_index]+1)*2:
            low = max_odd_index-odd_distance_list[max_odd_index]
            high = max_odd_index+odd_distance_list[max_odd_index]
        else:
            low = max_even_index-1-even_distance_list[max_even_index]
            high = max_even_index+even_distance_list[max_even_index]
        return s[low:high+1]


if __name__ == "__main__":
    # test_s = "jfbnhnjamsfsbsslcaaivnzryrrkcqmektqjnymeifxvvskicpxxrztysetlpucxfqccmeyptxxziqhacxatxjynmbblssyaxvcmbtyrtqfwxrwsgfrinfkczktytwglbrskeogamecvihkywnljnqfmrrnqcvopcoyroncwzhdqzvwdbtjmcocwljjvipabzorajqgiabqjeyasbrjvyjtdvgupqtmydfgdczaodyokxxarfboxifcltizhhntciffijclljvdfgpsojwmupgtrbquuzjdefnmxtcaborisjcsavucmuovlksonzvmmuvujzirioxdcadeioravjoyxhrqevfwmxacimtvbmfweqpvfijyuqrjfgejrnlmhvbbmbvviilsothgvaqgqtllonrqbsltwpikfrckdhttxzmbqmbhbjjwfddnrfwtafgjtuqyatkpcavokouftqwdzfclkckwzfwlozksgkrcyimvdhfrzlqqxnfhjkwfiewwqmbfyjdjematsvusmqxzwfyukqwlfzzyzlkqvgmq"
    # test_s ="321012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210012321001232100123210123210012321001232100123210123"
    # test_s = "aaaaaa"
    test_s = "cbbd"
    test_sol = Solution()
    sub_s = test_sol.manacher(test_s)
    sub_s_2 = test_sol.longestPalindrome(test_s)
    print (sub_s == sub_s_2)
    print(test_s)
    print(sub_s_2)
    print(sub_s)
    # print(sub_s)
