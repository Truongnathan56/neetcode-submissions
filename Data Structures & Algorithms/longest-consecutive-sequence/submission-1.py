class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) # Place nums into a set for easier lookup
        longest = 0

        for n in numSet:
            if (n - 1) not in numSet: # Does the previous number exist in the set?
                length = 0
                while (n + length) in numSet: # If the next number is in the set length increases
                    length += 1
                longest = max(length, longest) # Take the max of longest or the length
        return longest