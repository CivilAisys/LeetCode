# 此題關鍵在於找到旋轉點(及最小元素)
class Solution:
    def findMin(self, nums: list[int]) -> int:
        # 初始左右指針
        left = 0
        right = len(nums) - 1
        # 迴圈條件最後left == right  條件沒有等於只是在最後相等時不會再進行比較
        while left < right:
            mid = left + (right - left)//2
            # 與右邊元素比較確認旋轉點位置 且題目每元素皆為獨立不會重複故不會有重疊情況發生
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
