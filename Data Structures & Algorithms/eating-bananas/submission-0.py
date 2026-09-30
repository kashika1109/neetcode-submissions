class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # range of k is 1 < k < maxelement of piles max(piles), then do binary search there to find optimal k such that total of ceil(piles[i]/k) (hours to eat piles[i] bananas) <h
        l,r = 1, max(piles)

        res = r #if k = max(piles) element then it will take min hrs to eat all piles , hours = len(piles)
        while l<=r:
            k = (l+r) //2
            hr = 0
            for i in range(len(piles)):
                hr += math.ceil(piles[i]/k) #hours to eat all bananas of piles[i] at k rate pr hour
            if (hr > h): l = k+1
            elif (hr <= h):
                res = min(res,k)
                r = k-1 
        return res