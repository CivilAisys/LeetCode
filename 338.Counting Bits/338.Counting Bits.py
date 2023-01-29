# 解法1
# 時間: O(n) 空間:O(n)
def countBits(n: int) -> list[int]:
    if n == 0:
        return [0]

    # 初始化 創造出n個數值陣列且dp[1] = 1
    dp = [0 for _ in range(n+1)]
    dp[1] = 1

    # 計算 從2開始
    for i in range(2, n+1):
        # 偶數
        if i % 2 == 0:
            dp[i] = dp[i//2]
        else:
            dp[i] = dp[i//2] + 1
    return dp
