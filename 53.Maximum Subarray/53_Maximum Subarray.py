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


print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

# 解法2 題目要求使用分治法(Divide and Conquer Approach)
# 需要把數位一分為二，分別找出左邊和右邊的最大子數組之和，
# 然後還要從中間開始向左s右分別掃描(因為最大值可能橫跨中間點的左右)，
# 求出的最大值分別和左右兩邊得出的最大值相比較取最大的那一個
def maxSubArray2(nums: list[int]) -> int:
    return helper(nums, 0, len(nums) - 1)


def helper(nums: list[int], left: int, right: int) -> int:
    # 代表已經到達邊界 直接回傳邊界值
    if left >= right:
        return nums[left]
    # 中間值 從左到右最大  從又到左最大 從邊界向左右最大值
    mid = left + (right - left) // 2
    lmax = helper(nums, left, mid - 1)
    rmax = helper(nums, mid+1, right)
    mmax = nums[mid]
    t = mmax
    # 從中向左
    for index in range(mid-1, left - 1, -1):
        t += nums[index]
        mmax = max(mmax, t)
    t = mmax
    # 從中向右
    for index in range(mid+1, right+1):
        t += nums[index]
        mmax = max(mmax, t)

    return max(mmax, max(lmax, rmax))
