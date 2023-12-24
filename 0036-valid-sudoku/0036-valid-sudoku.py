class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        len_board = len(board)
        seen_rows = defaultdict(set)
        seen_columns = defaultdict(set)
        seen_sub_boxes = defaultdict(set)
        
        for m in range(len_board):
            for n in range(len_board):
                if m < 3 and n < 3:
                    sub_box = 1
                elif m < 3 and n >= 3 and n < 6:
                    sub_box = 2
                elif m < 3 and n >= 6 and n < 9:
                    sub_box = 3
                elif m >=3 and m < 6 and n < 3:
                    sub_box = 4
                elif m >=3 and m < 6 and n >= 3 and n < 6:
                    sub_box = 5
                elif m >=3 and m < 6 and n >= 6 and n < 9:
                    sub_box = 6
                elif m >=6 and m < 9 and n < 3:
                    sub_box = 7 
                elif m >=6 and m < 9 and n >= 3 and n < 6:
                    sub_box = 8  
                elif m >=6 and m < 9 and n >= 6 and n < 9:
                    sub_box = 9 
                item = board[m][n]
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
        
        