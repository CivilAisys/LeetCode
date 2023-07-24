class Solution:
    def uniquePaths(m: int, n: int) -> int:
        # 此保存到達最後一列的大於第一格的每一格所走的步數 且因m n至少為1  故result[0]至少為1
        # 若需要保存到達每一格的步數 至少需要維護一個2維陣列
        result = [0 for _ in range(n)]
        # 此為[0][n]的步數結果 因為機器人只能向右及向下走  所以到達第一列最後一行只會有一種方法
        result[0] = 1
        # i 為列 j 為行
        for i in range(m):
            for j in range(1, n):
                result[j] += result[j - 1]
        return result[n-1]

uniquePaths(3, 7)