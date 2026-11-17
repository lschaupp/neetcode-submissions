class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = [set() for _ in range(len(board))]
        grid = [set() for _ in range(len(board))]
        for idk, row in enumerate(board):
            print(idk, row)
            s = set()
            for idx, b in enumerate(row):
                if b == ".":
                    continue
                if b in s:
                    print("FALSE 1", b, s)
                    return False
                s.add(b)
                if b in col[idx]:
                    print("FALSE 2", b, col[idx])
                    return False
                col[idx].add(b)
                grid_idx = (idk // 3) * 3 + (idx // 3)
                if b in grid[grid_idx]:
                    return False
                grid[grid_idx].add(b)


        return True


        