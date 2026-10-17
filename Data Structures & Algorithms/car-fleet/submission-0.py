class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)] # Iterates through both at the same time to create a new pairs array
        stack = []
        for p, s in sorted(pair)[::-1]: # Reverse sorted order
            stack.append((target - p) / s) # Append the time of when that car arrives at the target
            if len(stack) >= 2 and stack[-1] <= stack[-2]: # If the stack len >= 2 and the new stack value is less than the previous value
                stack.pop() # Pop the top value 
    
        return len(stack)
        


        