class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result  = []
        max1 = max2 = -1 
        for i, num in enumerate(nums):
            if i >= k:
                if max1 == i - k: 
                    max1 = max2
                    max2 = -1
            if max1 == -1 or num > nums[max1]:
                max1 = i
                max2 = -1
            elif max2 == -1 or num > nums[max2]:
                max2 = i
            if i >= k-1:
                result.append(nums[max1])
        return result
        