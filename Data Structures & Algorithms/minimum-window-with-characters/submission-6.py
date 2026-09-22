class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countS, countT = {} , {}
        l = 0 #left = 0
        min_len = float('inf')
        min_str = [-1,-1]
        if t == "" : return ""
        
        for i in range(len(t)):
            countT[t[i]] = 1 + countT.get(t[i],0)

        have, need = 0, len(countT)
        for r in range(len(s)):
            countS[s[r]] = 1 + countS.get(s[r],0)
            if s[r] in countT and countS[s[r]] == countT[s[r]]: 
                have +=1

            while (have == need):
                #update our result          
                if r-l+1 < min_len:
                    min_len = r-l+1 #inf se sb chota hi hoga)
                    min_str = [l,r]
                #pop from window
                countS[s[l]] -= 1
                #reduce have if character was present in t and count now becomes less
                if (s[l] in countT and countS[s[l]] < countT[s[l]]): have -= 1 
                l +=1     

        l, r = min_str    
            
        return s[l:r+1] if min_len != float('inf') else ""


            

        