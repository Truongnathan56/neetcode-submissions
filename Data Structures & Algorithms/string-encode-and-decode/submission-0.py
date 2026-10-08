class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word # Ex: 4#Word
        return res
            


    def decode(self, s: str) -> List[str]:
        res, i = [], 0 # i is a pointer set to nothing
        while i < len(s):
            j = i # j is a pointer set to where i is at
            while s[j] != "#":
                j += 1 # Keep shifting j until a pound is found
            l = int(s[i:j]) # The length is from i to j, with j being exclusive
            # Appends the string from after # to the length of the string exclusive
            res.append(s[j + 1 : j + 1 + l])
            i = j + 1 + l # Gets i to the next string to be decoded
        return res