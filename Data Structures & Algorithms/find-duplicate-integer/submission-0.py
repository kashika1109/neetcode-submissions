class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #numbers in array are in range of 1 to len(nums) - 1 = number of indexes we have
        slow,fast = 0,0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast: break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2: return slow

        