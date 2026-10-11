class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")" : "(", "]" : "[", "}" : "{"} # Hashmap

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]: # If stack isn't empty & correct mapping
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
        