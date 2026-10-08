class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Duplicate detection
        cols = collections.defaultdict(set) # Shows which numbers occur in each [c]
        rows = collections.defaultdict(set) # Shows which numbers occur in each [r]
        squares = collections.defaultdict(set) # (r/3, c/3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": # If empty, skip
                    continue
                # If alrdy in rows, cols, or the specific 3 x 3 return false
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        return True