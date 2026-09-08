class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        i,j = 0, len(heights)-1
        while (i < j):
            width = j - i
            height = min(heights[i],heights[j])
            max_area = max(max_area, width * height)
            if(heights[i] < heights[j]): i+=1
            elif (heights[i] > heights[j]): j-=1
            elif (heights[i] == heights[j]):
                if(heights[i+1] >= heights[j-1]): i+=1
                else: j-=1
                   
        return max_area
                

        