class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums) # Pre initialize the array to have values of 1 up to the length of nums

        prefix = 1 # First set prefix = 1 
        for i in range(len(nums)):
            res[i] = prefix # Update prefix to the value in res[i]
            prefix *= nums[i] # Set prefix to itself times the value in nums

        postfix = 1 # Set postfix = 1
        for i in range(len(nums) - 1, -1, -1): # Iterate from the back
            res[i] *= postfix # Set res[i] to include the postfix product
            postfix *= nums[i] # Set postfix to itself times the value in nums
        
        return res
            


            