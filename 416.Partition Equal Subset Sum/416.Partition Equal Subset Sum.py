# 使用dp求解  dp[i] 表示列能否有若干個數位加總其和為target(i)
# 陣列所有數位和一定是偶數，不然根本無法拆成兩個和相同的子集合，
# 只需要算出原陣列的數位之和，然後除以2，就是 target，那麼問題就轉換為能不能找到一個非空子集合，使得其數位之和為 target
class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        # 加總  及  目標值
        total = sum(nums)
        target = total // 2
        # 若與1做位元運算  1為奇數 0為偶數 奇數直接返回False
        if total & 1:
            return False
        # dp陣列 預設值為False  target + 1是為了要包含dp[target]本身
        dp = [False for _ in range(target+1)]
        dp[0] = True

        # 開始進行遍歷並更新dp數組
        for num in nums:
            # 從 target 對每個num遍歷到num本身來更新dp陣列
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[target]
