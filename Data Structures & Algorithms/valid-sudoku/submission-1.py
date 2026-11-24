class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Check 'boxes'
        boxes = {0: {0: [], 1: [], 2: []}, 1: {0: [], 1: [], 2: []}, 2: {0: [], 1: [], 2: []}}

        for row_i, row in enumerate(board):
            for num_i, num in enumerate(row):
                if num.isalnum():
                    boxes[row_i // 3][num_i // 3].append(num)

        for i in range(3):
            for j in range(3):
                if not self.is_unique_arr(boxes[i][j]):
                    return False

        # Check rows:
        for row in board:
            if not self.is_unique_arr(row):
                return False

        # Check columns:
        col = []
        for i in range(9):
            for row in board:
                col.append(row[i])
            if not self.is_unique_arr(col):
                return False
            col = []

        return True

    def is_unique_arr(self, row: list[str]) -> bool:
        res = set()
        for ch in row:
            if ch.isalnum() and ch in res:
                return False
            res.add(ch)
        return True