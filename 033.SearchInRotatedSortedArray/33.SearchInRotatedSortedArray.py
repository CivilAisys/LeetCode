import math
# 題目要求BIG O 為 O(log n) 使用binary search
def search(nums: list[int], target: int) -> int:
    # 左中右索引
    lowIndex, highIndex, midIndex = 0, len(nums) - 1, -1

    while lowIndex <= highIndex:
        # 找出中心點index 長度可能是偶數  midIndex就會有小數點 故四捨五入
        midIndex = math.ceil(lowIndex + (highIndex - lowIndex)/2)

        # 終止條件
        if nums[midIndex] == target:
            return midIndex

        # 表示midIndex 在切分處的左側
        if nums[midIndex] > nums[lowIndex]:
            # 表示target可能在midIndex及lowIndex之間
            if target >= nums[lowIndex] and target < nums[midIndex]:
                highIndex = midIndex - 1
            else:
                lowIndex = midIndex + 1
        else:
            # 表示midIndex 在切分處的右側
            # 表示target可能在midIndex及highIndex之間
            if target > nums[midIndex] and target <= nums[highIndex]:
                lowIndex = midIndex + 1
            else:
                highIndex = midIndex - 1

    return -1


# search([4, 5, 6, 7, 0, 1, 2], 0)
search([3,1], 1)
