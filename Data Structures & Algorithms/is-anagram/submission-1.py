class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t): return False
        # countS , countT = {} , {}
        # for i in range(len(s)):
        #     countS[s[i]] = 1 + countS.get(s[i], 0)
        #     countT[t[i]] = 1 + countT.get(t[i], 0)
        
        # for val in countS:
        #     if countS[val] != countT.get(val, 0): return False
        # return True

        # return sorted(s) == sorted(t)
        if len(s) != len(t): return False
        countS = {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0)
        
        for val in range(len(t)):
            if countS.get(t[val], 0) > 0: countS[t[val]] = countS[t[val]] - 1

        for val in countS:
            if countS[val] > 0: return False
        return True
            

         

        