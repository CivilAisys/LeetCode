# 使用前綴和解題
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0  # 子數組個數
        curr_sum = 0  # 當前的總和
        prefix_sum = {0: 1}  # 前綴和的計數字典 初始須設定為{0:1}

        for num in nums:
            curr_sum += num
            # 檢查是否存在前綴和 curr_sum - k  當前前綴和與之前計算出前綴和可得出任意區間之和
            # 故若 curr_sum - k 存在  就將count加上curr_sum - k 出現次數
            if curr_sum - k in prefix_sum:
                count += prefix_sum[curr_sum - k]

            # 更新前綴和的計數
            prefix_sum[curr_sum] = prefix_sum.get(curr_sum, 0) + 1

        return count


test = Solution()
test.subarraySum(nums=[1, 1, 1, 1, 1], k=3)
