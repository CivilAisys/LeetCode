# 解法1 使用雙指針(索引) 索引i遍歷數組 索引j在num[i] != 0時進行調換並+1
def moveZeroes(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    j = 0
    for i in range(len(nums)):
        # 0為假值(Falsy) 兩兩調換且J+1
        if nums[i]:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
