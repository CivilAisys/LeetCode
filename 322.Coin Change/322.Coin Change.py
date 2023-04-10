# 解法1 dp
# 維護一個一維動態陣列 dp，其中 dp[i] 表示錢數為i時的最小硬幣數的找零，注意由於數位是從0開始的，
# 所以要多申請一位，數位大小為 amount+1，這樣最終結果就可以保存在 dp[amount] 中了
class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # amount + 1是因為值是從0開始的 且dp[0]=0 除dp[0]以外  初始皆為inf 避免無法更新(因為是取最小值)
        dp = [float('inf') for _ in range(amount + 1)]
        dp[0]= 0
        for amount in range(1, amount+1):
            for index in range(len(coins)):
                if coins[index] <= amount:
                    dp[amount] = min(dp[amount], dp[amount - coins[index]] + 1)
                
        return dp[amount] if dp[amount] <= amount else -1

test = Solution()

test.coinChange([1,2,5], 11)