class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None
        Do not return anything, modify board in-place instead.
        """

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        # Store existing numbers
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty.append((r, c))
                else:
                    d = board[r][c]
                    rows[r].add(d)
                    cols[c].add(d)
                    boxes[(r // 3) * 3 + (c // 3)].add(d)

        def solve(k):
            # All empty cells filled
            if k == len(empty):
                return True

            r, c = empty[k]
            b = (r // 3) * 3 + (c // 3)

            # Try digits 1 to 9
            for d in "123456789":

                if d in rows[r] or d in cols[c] or d in boxes[b]:
                    continue

                # Place digit
                board[r][c] = d
                rows[r].add(d)
                cols[c].add(d)
                boxes[b].add(d)

                # Recursively solve remaining cells
                if solve(k + 1):
                    return True

                # Backtrack
                board[r][c] = "."
                rows[r].remove(d)
                cols[c].remove(d)
                boxes[b].remove(d)

            return False

        solve(0)