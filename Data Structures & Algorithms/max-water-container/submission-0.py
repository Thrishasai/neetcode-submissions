class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0 
        j = len(heights) - 1 
        maxA = 0
        while i<j:
            vol = (j-i)*min(heights[i],heights[j])
            if heights[i]>heights[j]:
                j-=1
                
            elif heights[i]<heights[j]:
                i+=1
                
            else:
                i+=1
                j-=1
            maxA = max(maxA,vol)
        return maxA
        