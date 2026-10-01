class Solution:
    def findMin(self, nums: List[int]) -> int:
        #if our mid pointer is in left sorted section, we will go to search right
        #if its in right , we go to search left
        #if left<= right we store it  
        l ,r = 0, len(nums)-1
        res = nums[0]
        while l<=r:
            if (nums[l] <= nums[r]): res = min(res, nums[l])
            mid = (l+r) //2
            res = min(res,nums[mid])
            if (nums[l]<=nums[mid]): #we are in left sorted array
                l = mid+1
            elif (nums[l] > nums[mid]): #we are in right sorted array
                r = mid - 1    
        return res
        
