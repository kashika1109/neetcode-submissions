class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countS = { } #hashmap - number: occurences
        freq = [[] for i in range(len(nums)+1)] #array of counts - counts ke corres jo jo value hogi vo dalega
        final = []
        for i in range(len(nums)):
            countS[nums[i]] = countS.get(nums[i],0) + 1
        
        for n , c in countS.items(): # for key value in dictionary
            freq[c].append(n)
        
        for i in range(len(freq)-1,0,-1):
            for val in freq[i]:
                final.append(val)
                if len(final) == k: return final
             