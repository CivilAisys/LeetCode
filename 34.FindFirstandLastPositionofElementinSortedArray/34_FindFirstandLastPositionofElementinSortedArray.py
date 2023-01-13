# 解法1
# 題目要求算法複雜度必須為 O(log n)   nums為遞增陣列
# 要找出符合target的最左邊及最右邊的索引  如果target在nums內只有出現一次回傳同一索引
# 需要有兩個二分搜尋法 來找出符合最左邊及最右邊的含式
def searchRange(nums: list[int], target: int) -> list[int]:
    return [searchFirst(nums, target), searchLast(nums, target)]

# 返回nums內符合target的第一個索引
def searchFirst(nums: list[int], target: int) -> int:
    # 頭尾索引
    leftIndex, rightIndex = 0, len(nums) - 1
    result = -1
    while leftIndex <= rightIndex:
        # 中間索引  python兩個/ 當除不進時會找尋地板 如Math.floor
        midIndex = (leftIndex + rightIndex) // 2
        # 找到符合 更新midIndex
        if nums[midIndex] == target:
            result = midIndex

        if nums[midIndex] >= target:
            rightIndex = midIndex - 1
        else:
            leftIndex = midIndex + 1

    return result

# 返回nums內符合target的最後一個索引
def searchLast(nums: list[int], target: int) -> int:
    # 頭尾索引
    leftIndex, rightIndex = 0, len(nums) - 1

    while leftIndex <= rightIndex:
        # 中間索引  python兩個/ 當除不進時會找尋地板 如Math.floor
        midIndex = (leftIndex + rightIndex) // 2

        if nums[midIndex] > target:
            rightIndex = midIndex - 1
        else:
            leftIndex = midIndex + 1

    # left right index最後回限縮至同一索引  找到第一個>target的索引  比對該索引- 1與target是否一致 回傳該所引-1
    leftIndex -= 1
    if leftIndex >= 0 and nums[leftIndex] == target:
        return leftIndex

    return -1


# 解法2
def searchRange1(nums: list[int], target: int) -> list[int]:
    left = binSearch(nums, target , True)
    right = binSearch(nums, target, False)
    return [left, right]
#若leftBias == True  表示要找尋最左側符合target的索引值
def binSearch(nums: list[int], target: int, leftBias : bool) -> int:
    l, r = 0, len(nums) - 1
    i = -1
    while l <= r:
        m = (l+r)//2
        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            # 此為相等時  更新i = m  並依照leftBias更新左或右索引
            i = m
            if leftBias:
                r = m - 1
            else:
                l = m + 1
    return i




