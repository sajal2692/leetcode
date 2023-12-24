class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        len_board = len(board)
        seen_rows = defaultdict(set)
        seen_columns = defaultdict(set)
        seen_sub_boxes = defaultdict(set)
        
        for m in range(len_board):
            for n in range(len_board):
                item = board[m][n]
                sub_box = (m // 3, n // 3)
                if item == ".":
                    continue
                if item in seen_rows[m]:
                    return False
                if item in seen_columns[n]:
                    return False
                if item in seen_sub_boxes[sub_box]:
                    return False
                seen_sub_boxes[sub_box].add(item)
                seen_rows[m].add(item)
                seen_columns[n].add(item)
        return True
        
        