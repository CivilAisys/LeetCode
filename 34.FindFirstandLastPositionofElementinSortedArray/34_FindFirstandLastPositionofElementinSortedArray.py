import math
#題目要求算法複雜度必須為 O(log n)   nums為遞增陣列
def searchRange(nums: list[int], target: int) -> list[int]:
    #左中右索引
    firstIndex, midIndex, lastIndex = 0, len(nums) - 1, -1
    #結果陣列
    result = []

    while firstIndex <= lastIndex:
        #計算中間索引 無條件進位
        midIndex = math.ceil(firstIndex + (lastIndex - firstIndex)/2)

        #終止條件
        if nums[midIndex] == target:
            result.append(midIndex)
        







