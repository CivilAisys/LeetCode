# 解法1 如同斐波那契數列 推導出公式  dp[n] = dp[n-1] + dp[n-2]
def climbStairs(n: int) -> int:
    if n <= 1:
        return 1
    # dp代表爬到n+1階所有可能的步數
    dp = [1,2]

    for index in range(2, n):
        dp.append(dp[index-1] + dp[index-2])

    return dp[n-1]


# 解法2 如同斐波那契數列 推導出公式  dp[n] = dp[n-1] + dp[n-2] 使用遞迴
def climbStairs1(n: int) -> int:
    #使用cache去緩存計算過的結果  避免重複計算導致超時
    cache = {}
    def helper_function(n):
        if n <= 1:
            cache[n] = 1
            return 1

        if n in cache:
            return cache[n]
        else:
            num = helper_function(n-1) + helper_function(n-2)
            cache[n] = num
            return num
    
    helper_function(n)
    return cache[n]

climbStairs1(1)

