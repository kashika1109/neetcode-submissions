class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) #default value of entire array is 0
        stack = [] #pair: temp, index

        for i,t in enumerate(temperatures): #get index and temp side by side
            while stack and t > stack[-1][0]: #current temp is > stack ka top vala temp 
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd #result ke vo index ko update krdo jo choti value pr tha
            stack.append([t,i]) #if less current temp < stack top's temp , push
        return res



    
        