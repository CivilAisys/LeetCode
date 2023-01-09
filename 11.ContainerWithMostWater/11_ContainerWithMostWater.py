# 解法1  雙指針  從左右向內縮小並比較左右兩端點高度
# 較低的向內縮進 相等時左端右移
def maxArea(height: list[int]) -> int:
    # 最大容積
    maxVoulume = 0
    # 頭尾索引
    left = 0
    right = len(height) - 1
    # 迴圈進行計算
    while right > left:
        # 比對當前計算容積與maxVolume誰大
        maxVoulume = max(maxVoulume, min(
            height[left], height[right]) * (right - left))
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1
    return maxVoulume


maxArea([10, 14, 10, 4, 10, 2, 6, 1, 6, 12])
