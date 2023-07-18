class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        row_zeroes = [False] * rows  # 用於標記每一列是否需要設置為0
        col_zeroes = [False] * cols  # 用於標記美意行是否需要設置為0

        # 第一次遍歷矩陣 標記出需要設置為0的行列
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    row_zeroes[i] = True
                    col_zeroes[j] = True

        # 第二次遍歷矩陣，將需要設置為 0 的行和列的元素設置為 0
        for i in range(rows):
            for j in range(cols):
                if row_zeroes[i] or col_zeroes[j]:
                    matrix[i][j] = 0
