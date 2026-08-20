class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        num_rows, num_cols = len(matrix), len(matrix[0])
        self.sum_mat = [
            [0] * (num_cols + 1) for r in range(num_rows+1)
        ]

        for r in range(num_rows):
            prefix = 0
            for c in range(num_cols):
                prefix += matrix[r][c]
                above = self.sum_mat[r][c+1]
                self.sum_mat[r+1][c+1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1

        return (
            self.sum_mat[row2][col2] 
            - self.sum_mat[row1-1][col2]
            - self.sum_mat[row2][col1-1]
            + self.sum_mat[row1-1][col1-1]
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)