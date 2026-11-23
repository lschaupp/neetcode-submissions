class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 1 * len(heights)

        # Use a stack to keep track of indices of increasing bar heights
        # When a lower bar is found, pop from the stack and calc area
        stack = []
        maxArea = 0
        heights.append(0)

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea, height*width)
            stack.append(i) # Push current index to stack
        return maxArea


