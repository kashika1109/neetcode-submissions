class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        top_r , bottom_r = 0, rows - 1
        while top_r <= bottom_r:
            mid_r = (top_r + bottom_r) // 2
            if target > matrix[mid_r][-1]:
                top_r = mid_r + 1
            elif target < matrix[mid_r][0]:
                bottom_r = mid_r  - 1
            else:
                break;
        
        if not (top_r <= bottom_r): return False
        l, r = 0, cols -1
        mid_r = (top_r + bottom_r) // 2
        while l<=r:
            mid = (l+r) // 2
            if(matrix[mid_r][mid] == target): return True
            elif(matrix[mid_r][mid] < target): l = mid + 1
            else: r = mid-1
        return False
            


        