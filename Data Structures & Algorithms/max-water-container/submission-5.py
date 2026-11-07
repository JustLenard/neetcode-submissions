class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        
        i, j = 0 , len(heights) - 1

        width = j - i 

        while i < j:
            local_area = min(heights[i], heights[j]) * width
            max_area = max(local_area, max_area)

            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
            
            width -= 1
        return max_area
