# 解法1 使用dp
# dp[i] 表示以 nums[i] 為結尾的最長上升子序列的長度(此題可以跳躍  不一定要連續的)
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        nums_length = len(nums)
        dp = [1 for _ in range(nums_length)]  # dp數組 預設最小為1
        # 只要 nums[i] > nums[j] dp[i]就進行比對更新 dp[i] = max(dp[i],dp[j] + 1)
        for i in range(1, nums_length):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)
