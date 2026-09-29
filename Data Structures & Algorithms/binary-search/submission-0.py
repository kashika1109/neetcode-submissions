class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums) - 1
        while l <= r:
            mid = (r + l) // 2 #returns quotient in integer form

            if (nums[mid] == target): return mid
            elif (nums[mid] < target):
                l = mid + 1
                continue;
            elif(nums[mid] > target):
                r = mid - 1
                continue;
        return -1
        