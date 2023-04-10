# 解法1 雙指標
# 若給定數組皆為降序  代表為排列的最後一組 則返回最小的排序(升序)
# 此題關鍵在於如何找到下一個更大的排列
# 右到左遍歷數字，找到第一個不符合升序排列的位置。這個位置右側的數字都已經是降序排列的，
# 如果希望得到下一個更大的排列，那麼需要重新排列這些數字。可以從這些數字中找到比該位置數字大的最小數字，並交換它們的位置，然後將這些數字排序。
class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # 從右到左找到第一個不符合降序排列的位置
        i = n - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        # 若數列全為降序排列 代表該值為最大  下一個為最小值(升序排列)
        if i < 0:
            nums.sort()
            return
        # 從右到左找到第一個比nums[i]還要大的數字
        j = n - 1
        while j >= 0 and nums[j] <= nums[i]:
            j -= 1
        # 將nums[j] 與 nums[i]兩者交換並降nums[i]後的數值進行排列即為結果
        nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:] = reversed(nums[i+1:])