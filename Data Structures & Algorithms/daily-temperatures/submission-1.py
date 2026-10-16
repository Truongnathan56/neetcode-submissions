class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Monotonically Decreasing Stack

        result = [0] * len(temperatures) # Initialize result with values of 0
        stack = [] # Includes [temperature, index]
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: # If the stack is not empty and t > stack[-1] temp
                stackT, stackInd = stack.pop() # Pop and save the temp and index value
                result[stackInd] = (i - stackInd) # Find # of days it took to find higher temp
            stack.append([t, i])
        
        return result



        