# 解法1 翻轉法
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        #翻轉前半部分
        nums[:n-k] = reversed(nums[:n-k])
        #翻轉後半部分
        nums[n-k:] = reversed(nums[n-k:])
        #全部翻轉
        nums[:] = reversed(nums[:])