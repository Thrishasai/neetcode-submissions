class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        heights.append(0)

        for R, height in enumerate(heights):
            L = R
            while stack and stack[-1][1] > height:
                L, prev_height = stack.pop()
                maxArea = max(maxArea, prev_height * (R - L))
            stack.append((L, height))

        return maxArea
        