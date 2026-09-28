class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) #default value of entire array is 0
        stack = [] #pair: temp, index

        for i,t in enumerate(temperatures): #get index and temp side by side
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append([t,i])
        return res



    
        