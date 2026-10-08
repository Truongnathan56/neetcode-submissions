from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # maps character count to the anagram list
        for s in strs: # Loops through strings in str
            count = [0] * 26 # Creates an array with 0 for every letter in the alphabet
            for c in s: # Loops through characters per string
                count[ord(c) - ord("a")] += 1 # ASCII value conversion for our array

            res[tuple(count)].append(s) # Appends if the count array is the same
        
        return list(res.values()) # Converts the dict values to list of lists
        