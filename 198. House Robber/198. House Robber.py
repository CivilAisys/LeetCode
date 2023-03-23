# 解法1  使用dynamic programming
# 令dp[i] 為前i個房屋中能盜取的最大金額
# 如果只有一個房屋，那麼 dp[0] = nums[0]。
# 如果有兩個房屋，那麼 dp[1] = max(nums[0], nums[1])。如果有多於兩個的房屋，那麼對於第 i 個房屋，有兩種選擇：
# 直接偷第 i 個房屋，那麼能夠盜取到的最大金額為 dp[i-2] + nums[i]。不偷第 i 個房屋，那麼能夠盜取到的最大金額為 dp[i-1]。
# 可以得到狀態轉移方程：dp[i] = max(dp[i-2] + nums[i], dp[i-1])
class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)
        # 只有1間房屋時
        if n == 1:
            return nums[0]

        dp = [0] * n  # dp數組 dp[i] 為前i個房屋中能盜取的最大金額
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        # 開始進行遍歷  dp的狀態轉移方程為 dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        for i in range(2, n):
            dp[i] = max(dp[i-2]+nums[i], dp[i-1])
        return dp[n-1]
