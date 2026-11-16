class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # cols = defaultdict(set)
        # rows = defaultdict(set)
        # squares = defaultdict(set)
        # for r in range(9):
        #     for c in range(9):
        #         if board[r][c] == ".":
        #             continue 
        #         if (board[r][c] in rows[r] 
        #         or board[r][c] in cols[c] or 
        #         board[r][c] in squares[(r//3, c//3)]):
        #             return False
        #         cols[c].add(board[r][c])
        #         rows[r].add(board[r][c])
        #         squares[(r//3, c//3)].add(board[r][c])
        #optimal solution 
        cols = [0] * 9
        rows = [0] * 9
        squares = [0] * 9
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue 
                val = int(board[r][c])-1
                bit = 1 << val 
                sq_index = (r//3)*3 + (c//3)
                if (bit & rows[r]) or (bit & cols[c]) or (bit & squares[sq_index]):
                    return False
                    
                cols[c] |= bit
                rows[r] |= bit
                squares[sq_index] |= bit 
        return True

