class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = set()
        l = 0
        count = 0
        for r in range(len(s)):
            while s[r] in result:
                result.remove(s[l])
                l+=1
            result.add(s[r])
            count = max (count, r-l+1)
        return count 


        