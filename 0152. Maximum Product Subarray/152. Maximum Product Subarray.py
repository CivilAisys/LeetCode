# 解法1 dp
# 要找出連續陣列的最大乘積  因為數列內有負數  故每個可能的子陣列都維護最大最小值
# 因為有負數的關係  最大值*負數 為小值  最小值*負數為大值  故num[i]為負數時  大小值需要進行調換
# 計算以該元素結尾的子數組中的最大乘積和最小乘積，然後更新全局的最大乘積
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max_product = nums[0]  # 全局最大值
        cur_max = nums[0]  # 當前最大值
        cur_min = nums[0]  # 當前最小值
        # 開始對數組進行遍歷
        for i in range(1, len(nums)):
            # nums[i] 為負時  最大最小值要做交換
            if nums[i] < 0:
                cur_max, cur_min = cur_min, cur_max
            # 更新以i索引為節為的子數組的最大最小
            cur_max = max(nums[i], nums[i]*cur_max)
            cur_min = min(nums[i], nums[i]*cur_min)
            # 更新全局最大值
            max_product = max(max_product, cur_max)
        return max_product
