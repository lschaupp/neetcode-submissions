class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = [set() for _ in range(len(board))]
        grid = [set() for _ in range(len(board))]
        for row_idx, row in enumerate(board):
            s = set()
            for col_idx, b in enumerate(row):
                if b == ".":
                    continue
                if b in s:
                    return False
                s.add(b)
                if b in col[col_idx]:
                    return False
                col[col_idx].add(b)
                grid_idx = (row_idx // 3) * 3 + (col_idx // 3)
                if b in grid[grid_idx]:
                    return False
                grid[grid_idx].add(b)
        return True


        