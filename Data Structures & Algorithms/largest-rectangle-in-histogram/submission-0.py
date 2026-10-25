class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0 # Initialize max area as 0
        stack = [] # Keep track of the index and height

        for i, h in enumerate(heights):
            start = i # Start at i, not sure if it can be extended backwards
            while stack and stack[-1][1] > h: # While not empty and top height value > h
                index, height = stack.pop() # Pop the current index and height
                maxArea = max(maxArea, height * (i - index)) # Check if what we pop is max
                start = index # Extend start index backwards to what was just popped
            stack.append((start, h))
        
        # For the remaining items in the stack
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
            
        return maxArea
                