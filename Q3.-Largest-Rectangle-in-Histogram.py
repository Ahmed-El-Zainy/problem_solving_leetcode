1class Solution:
2    def largestRectangleArea(self, heights: List[int]) -> int:
3        stack = []
4        max_area = 0
5        heights.append(0)
6        for i in range(len(heights)):
7            while stack and heights[stack[-1]] > heights[i]:
8                height = heights[stack.pop()]
9                width = i if not stack else  i - stack[-1] -1
10                max_area = max(max_area , (height * width))
11            stack.append(i)
12        return max_area