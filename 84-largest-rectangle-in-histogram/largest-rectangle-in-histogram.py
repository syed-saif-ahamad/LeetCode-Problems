class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0 
        n = len(heights)
        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                height = heights[stack.pop()]
                if stack:
                    width = i - stack[-1] -1
                else:
                    width = i
                area = height * width 
                max_area = max(max_area,area)
            stack.append(i)
        while stack:
            height = heights[stack.pop()]
            if stack:
                width = n - stack[-1] -1
            else:
                width = n
            area = height * width 
            max_area = max(max_area,area)
        return max_area