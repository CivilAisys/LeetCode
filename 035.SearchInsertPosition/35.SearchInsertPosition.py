# 題目要求 複雜度為O(log n) nums內為不重複數值  若target in nums return index or 需插入的索引
def searchInsert(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    
    #找尋第一個大於target的索引  回傳索引 - 1
    while left <= right:
        mid = (left + right) // 2

        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left =  mid + 1
        else:
            #相等　直接回傳mid
            return mid

    return left




