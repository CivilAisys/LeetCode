import math
# 解法1   使用 kadane's algorithm  此為最大子數列問題
def maxSubArray(nums: list[int]) -> int:
    # 當前最大總和 , 當前加總
    max_Sum = -math.inf
    sum = 0

    for index in range(len(nums)):
        # 先將當前數字加至sum內
        sum += nums[index]
        # 判斷當前最大
        max_Sum = max(max_Sum, sum)
        # 若sum < 0 時  重置sum為0
        if sum < 0:
            sum = 0

    return max_Sum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
