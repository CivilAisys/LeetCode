class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        if not matrix:
            return 0

        rows = len(matrix)  # 列數
        cols = len(matrix[0])  # 行數
        max_side = 0  # 紀錄最大邊長  最後回傳平方及可
        # dp 數組 將行列都+1避免越界問題
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        # 遍歷dp數組
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    # 當前元素為1時 因為dp數組的第一列及第一行為多創建出來避免越界的 故實際i j 於 dp數組內都要+1
                    # 正方形取左邊左上上方三者最小值+1  因為正方形邊長由最小邊決定 +1是因為至少本身長度就為1
                    dp[i+1][j+1] = min(dp[i][j], dp[i+1][j], dp[i][j+1]) + 1
                    max_side = max(max_side, dp[i+1][j+1])

        return max_side * max_side
