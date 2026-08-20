class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # product = 1
        # index0 = -1
        # for i in range(len(nums)):
        #     if (nums[i] != 0 ):product = product * nums[i]
        #     else: index0 = i
        
        # if (index0 < 0 ):
        #     result = []
        #     for i in range(len(nums)):
        #         result.append(product // nums[i])
        #     return result
        # else:
        #     result = []
        #     for i in range(len(nums)):
        #         if (i == index0): result.append(product)
        #         else: result.append(0)
        #     return result
        res = [1] * len(nums)
        prefix = 1 #default first prefix will be 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        # eg you have [1 ,2, 3] input - result prefix iteration becomes = [1,1*1 = 1,1*2 =2]
        postfix = 1
        for i in range(len(nums)-1, -1, -1): #back to front
            res[i] *= postfix
            postfix *= nums[i]  # if result was [1,1,2] and this iteration makes it [6*1,3*1,1*2]
        return res

        
