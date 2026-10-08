from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # Dictionary to keep track of the value {number: frequency}
        freq = [[] for i in range(len(nums) + 1)] # Make a 2d list for each bucket that holds frequency per occurrence

        # For each occurrence in the list, add to the count in the hashmap otherwise put 0
        for n in nums:
            count[n] = count.get(n, 0) + 1 # Adds 1 to the number of times it has occurred
        
        # Place the items into the correct bucket marked by frequency
        for n, c in count.items():
            freq[c].append(n)

        # (1, 2), (1, 2), (3, 1)
        # [[],[3],[1, 2],[]]

        res = []
        for i in range(len(freq) - 1, 0, -1): # Reverse iterate through the buckets
            for n in freq[i]: # For each item in the buckets
                res.append(n) # Append until k top is found then return
                if len(res) == k:
                    return res

