class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R, C = len(matrix), len(matrix[0])
        t, b = 0, R - 1

        # Binary search on the rows
        while t <= b:
            row = (t + b) // 2
            if target > matrix[row][-1]: # Check the largest value in the row
                t = row + 1
            elif target < matrix[row][0]: # Check the smallest value in the row
                b = row - 1
            else:
                break
        
        # If none of the rows work, return false immediately
        if not (t <= b):
            return False
        
        row = (t + b) // 2
        l, r = 0, C - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False
