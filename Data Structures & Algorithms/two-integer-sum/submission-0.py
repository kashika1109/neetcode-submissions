class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        countS = {}
        for index in range(len(nums)):
            difference = target - nums[index]
            if (difference in countS and countS[difference] != index):
                if(countS[difference] > index): return [index, countS[difference]]
                else: return [countS[difference],index]

            countS[nums[index]] = index
        return